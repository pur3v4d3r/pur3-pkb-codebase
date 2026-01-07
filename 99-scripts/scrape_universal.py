import re
import csv
import os
import time
import requests
import sys

class UniversalPaperScraper:
    def __init__(self, markdown_file_path):
        self.markdown_file_path = markdown_file_path
        # Create output dir in the same folder as the script
        base_dir = os.path.dirname(os.path.abspath(markdown_file_path))
        self.output_dir = os.path.join(base_dir, "downloaded_papers")
        
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    def sanitize_filename(self, title):
        clean_name = re.sub(r'[^\w\s-]', '', title)
        clean_name = re.sub(r'\s+', ' ', clean_name).strip()
        return clean_name[:150]

    def convert_to_pdf_url(self, url):
        url = url.strip()
        if "arxiv.org/abs/" in url:
            return url.replace("/abs/", "/pdf/") + ".pdf"
        elif "openreview.net/forum" in url:
            return url.replace("/forum", "/pdf")
        elif "aclanthology.org" in url and not url.endswith(".pdf"):
            return url.strip("/") + ".pdf"
        elif "github.com" in url:
            return None 
        return url

    def detect_format_and_parse(self):
        try:
            with open(self.markdown_file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                lines = content.splitlines()
        except Exception as e:
            print(f"❌ Critical Error reading file: {e}")
            return []

        type_a_count = content.count('[[Paper]')
        type_b_count = len(re.findall(r'^\s*[-*]\s+\[.+?\]\(.+?\)', content, re.MULTILINE))

        if type_a_count > type_b_count:
            print("👉 Detected Format: Block Style")
            return self.parse_block_style(lines)
        else:
            print("👉 Detected Format: List Style")
            return self.parse_standard_list_style(lines)

    def parse_block_style(self, lines):
        papers = []
        current_category = "Uncategorized"
        current_paper = {}
        
        category_pattern = re.compile(r'^##\s+(.+)')
        title_pattern = re.compile(r'\*\*(.+?)\*\*')
        link_pattern = re.compile(r'\[\[Paper\]\((.+?)\)\]')

        for i, line in enumerate(lines):
            line = line.strip()
            cat_match = category_pattern.match(line)
            if cat_match:
                current_category = cat_match.group(1)
                continue
            
            title_match = title_pattern.search(line)
            if title_match and line.startswith("**"):
                if current_paper.get('url'): papers.append(current_paper)
                current_paper = {'category': current_category, 'title': title_match.group(1), 'url': None}

            if current_paper:
                link_match = link_pattern.search(line)
                if link_match: current_paper['url'] = link_match.group(1)

        if current_paper.get('url'): papers.append(current_paper)
        return papers

    def parse_standard_list_style(self, lines):
        papers = []
        current_category = "Uncategorized"
        item_pattern = re.compile(r'^\s*[-*]\s+\[(.+?)\]\((.+?)\)')
        category_pattern = re.compile(r'^##+\s+(.+)')

        for line in lines:
            line = line.strip()
            cat_match = category_pattern.match(line)
            if cat_match:
                current_category = cat_match.group(1)
                continue

            match = item_pattern.match(line)
            if match:
                url = match.group(2)
                if not url.startswith("#"):
                    papers.append({'category': current_category, 'title': match.group(1), 'url': url})
        return papers

    def download_paper(self, paper):
        original_url = paper['url']
        if not original_url: return

        pdf_url = self.convert_to_pdf_url(original_url)
        if not pdf_url: return

        safe_filename = self.sanitize_filename(paper['title']) + ".pdf"
        file_path = os.path.join(self.output_dir, safe_filename)

        if os.path.exists(file_path):
            print(f"⏭️  Exists: {safe_filename[:30]}...")
            return

        print(f"⬇️  Downloading: {paper['title'][:40]}...")
        try:
            response = requests.get(pdf_url, headers=self.headers, timeout=30, stream=True)
            if response.status_code == 200:
                with open(file_path, 'wb') as f:
                    for chunk in response.iter_content(chunk_size=8192):
                        f.write(chunk)
                time.sleep(2)
            else:
                print(f"❌ Failed ({response.status_code})")
        except Exception as e:
            print(f"❌ Error: {str(e)}")

    def run(self):
        print(f"📂 processing: {os.path.basename(self.markdown_file_path)}")
        papers = self.detect_format_and_parse()
        print(f"📝 Found {len(papers)} papers.")
        print("🚀 Starting downloads...")
        for paper in papers:
            self.download_paper(paper)

def get_target_file():
    """Auto-detects markdown files in the script's directory"""
    # Get the directory where THIS script lives
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # List all files in that directory
    files = [f for f in os.listdir(script_dir) if f.endswith('.md')]
    
    if not files:
        print(f"❌ No .md files found in {script_dir}")
        print("Make sure the markdown file is in the same folder as this script!")
        return None
    
    if len(files) == 1:
        return os.path.join(script_dir, files[0])
    
    print("Found multiple markdown files:")
    for i, f in enumerate(files):
        print(f"{i + 1}. {f}")
    
    try:
        choice = int(input("Enter number of file to process: ")) - 1
        return os.path.join(script_dir, files[choice])
    except:
        return None

if __name__ == "__main__":
    target_file = get_target_file()
    
    if target_file:
        scraper = UniversalPaperScraper(target_file)
        scraper.run()
    else:
        input("Press Enter to exit...")