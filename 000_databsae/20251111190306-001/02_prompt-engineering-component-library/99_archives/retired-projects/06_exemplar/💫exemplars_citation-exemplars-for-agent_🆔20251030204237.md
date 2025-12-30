---
title: 💫Exemplars_Citation-Exemplars-for-Agent_🆔20251030204237
id: 20251030204242
aliases:
  - "[Component-Alias]"
type: 🧩component
status: 🌱seedling
last-used: ❔
priority: ❔
created: 2025-10-30T20:42:42
source: 🦖pur3v4d3r
url: https://gemini.google.com/app/cfae1182967a068b
tags:
  - prompt-component-library
  - component
  - component/type/exemplar
description: ❔
version: '"1.0"'
success-rating: ❔
---

```component
---
id: prompt-block-🆔20251030204237
---

-----

## 0. Blank (Exemplar)

> [!cite]
> **Bibliographic Information**
> - **Source Type**:: 
> - **Title**:: 
> - **Author(s)**:: 
> - **Year**:: 
> - **Publisher / Journal**:: 
> - **Volume / Issue**:: 
> - **Page(s)**:: 
> - **URL / DOI**:: 
> - **Date Accessed**::

-----

## 📚 1. Book (Print)

For a standard print book, the mapping is straightforward. The `Publisher / Journal` field is used for the publisher's name. The `Volume / Issue`, `URL / DOI`, and `Date Accessed` fields are typically left blank as they do not apply. The `Page(s)` field is used for the specific page number where the quote is located.

> [!cite]
> **Bibliographic Information**
>
>   - **Source Type**:: Book
>   - **Title**:: Cosmos
>   - **Author(s)**:: Sagan, Carl
>   - **Year**:: 1980
>   - **Publisher / Journal**:: Random House
>   - **Volume / Issue**::
>   - **Page(s)**:: p. 42
>   - **URL / DOI**::
>   - **Date Accessed**::

-----

## 🧾 2. Journal Article

This is where your template's flexible fields shine. The `Publisher / Journal` field is now used for the name of the journal (e.g., *Nature*, *The Astrophysical Journal*). The `Volume / Issue` field is critical here and should be filled in. The `Page(s)` field should refer to the specific page of the quote, though some people use it for the full article page range. For a quote, the specific page is more useful. A DOI (Digital Object Identifier) is the most stable way to link to an article, so it is preferred over a URL.

> [!cite]
> **Bibliographic Information**
>
>   - **Source Type**:: Journal Article
>   - **Title**:: A Relativistic Jet from a Black Hole X-ray Binary
>   - **Author(s)**:: Gallo, E.; Fender, R. P.; Pooley, G. G.
>   - **Year**:: 2003
>   - **Publisher / Journal**:: Nature
>   - **Volume / Issue**:: 425(6960)
>   - **Page(s)**:: p. 805
>   - **URL / DOI**:: 10.1038/nature02026
>   - **Date Accessed**::

-----

## 🌐 3. Website / Webpage

When citing a website, the `Author(s)` field may be a person's name or an organization (e.g., NASA, Google). The `Publisher / Journal` field should be used for the name of the website itself. The `Year` should be the date the article or page was published (if available). The `Page(s)` field is often not applicable, so you can use it to store a paragraph number (e.g., `para. 5`) or a specific section heading. The `URL / DOI` field is essential, and the `Date Accessed` field is critical, as websites are not stable and can change or be removed.

> [!cite]
> **Bibliographic Information**
>
>   - **Source Type**:: Website
>   - **Title**:: What Is a Black Hole?
>   - **Author(s)**:: NASA
>   - **Year**:: 2024
>   - **Publisher / Journal**:: NASA Science
>   - **Volume / Issue**::
>   - **Page(s)**:: "Event Horizon" section
>   - **URL / DOI**:: `https://science.nasa.gov/universe/black-holes/what-is-a-black-hole/`
>   - **Date Accessed**:: 2025-10-27

-----

## 📖 4. Chapter in an Edited Book

This can be complex, but your template handles it. The `Title` field should be for the **chapter title**, and the `Author(s)` field should be for the **chapter's author(s)**. The `Publisher / Journal` field is then used to store the information about the *book itself*, including the book's title and the editor(s).

> [!cite]
> **Bibliographic Information**
>
>   - **Source Type**:: Book Chapter
>   - **Title**:: The Nature of Knowledge
>   - **Author(s)**:: Smith, John A.
>   - **Year**:: 2022
>   - **Publisher / Journal**:: In *The Philosophy of Information* (Ed. R. Johnson), Oxford University Press
>   - **Volume / Issue**::
>   - **Page(s)**:: p. 142
>   - **URL / DOI**::
>   - **Date Accessed**::

-----

## ▶️ 5. YouTube Video (or other media)

For modern media, you can adapt the fields logically. The `Author(s)` field is best used for the channel name. The `Publisher / Journal` field is for the platform (e.g., YouTube, Vimeo). The `Page(s)` field becomes a `Timestamp` for the exact location of the quote. The `Year` is the upload year.

> [!cite]
> **Bibliographic Information**
>
>   - **Source Type**:: YouTube Video
>   - **Title**:: Your First Obsidian Plugin: A Beginner's Guide
>   - **Author(s)**:: PKM Explained
>   - **Year**:: 2024
>   - **Publisher / Journal**:: YouTube
>   - **Volume / Issue**::
>   - **Page(s)**:: 12:31
>   - **URL / DOI**:: `https://www.youtube.com/watch?v=...`
>   - **Date Accessed**:: 2025-10-27

---

## 📰 6. Newspaper Article (Online or Print)

Use this for articles from news publications like *The New York Times* or *The Guardian*. The `Publisher / Journal` field holds the newspaper's title, and the `Page(s)` field is for the section and page number (e.g., `A12`) if in print.

> [!cite]
> **Bibliographic Information**
> - **Source Type**:: Newspaper Article
> - **Title**:: For Biden, a New Virus Dilemma: How to Handle a Looming Glut of Vaccine
> - **Author(s)**:: LaFraniere, Sharon; Weiland, Noah
> - **Year**:: 2021-03-26
> - **Publisher / Journal**:: The New York Times
> - **Volume / Issue**:: 
> - **Page(s)**:: A1
> - **URL / DOI**:: `https://www.nytimes.com/2021/03/26/us/biden-coronavirus-vaccine.html`
> - **Date Accessed**:: 2025-10-27

---

## 🎙️ 7. Podcast Episode

This is for audio-first sources. The `Author(s)` is the host, `Title` is the episode title, and `Publisher / Journal` is the name of the podcast series itself. The `Page(s)` field is perfect for a `Timestamp`.

> [!cite]
> **Bibliographic Information**
> - **Source Type**:: Podcast Episode
> - **Title**:: The Science of Gratitude & How to Build a Gratitude Practice
> - **Author(s)**:: Huberman, Andrew (Host)
> - **Year**:: 2022-11-21
> - **Publisher / Journal**:: Huberman Lab
> - **Volume / Issue**:: Ep. 95
> - **Page(s)**:: 00:45:10
> - **URL / DOI**:: `https://www.hubermanlab.com/episode/the-science-of-gratitude-and-how-to-build-a-gratitude-practice`
> - **Date Accessed**:: 2025-10-27

---

## 🎓 8. Thesis or Dissertation

This is for academic work produced by a graduate student. The `Publisher / Journal` field is used for the university/institution that granted the degree. The `Volume / Issue` field is a good place to specify the degree type (e.g., "Doctoral dissertation" or "Master's thesis").

> [!cite]
> **Bibliographic Information**
> - **Source Type**:: Dissertation
> - **Title**:: Factors Influencing Customer Satisfaction at a Fast Food Hamburger Chain
> - **Author(s)**:: Kabir, J. M.
> - **Year**:: 2016
> - **Publisher / Journal**:: Wilmington University
> - **Volume / Issue**:: Doctoral dissertation
> - **Page(s)**:: p. 78
> - **URL / DOI**:: ProQuest Dissertations & Theses Global (Publication No. 10169573)
> - **Date Accessed**:: 2025-10-27

---

## 🗣️ 9. Lecture / Speech / Presentation

This is for a live or recorded talk. The `Author(s)` is the speaker. The `Publisher / Journal` field is for the event name (e.g., "TED 2023"), and the `Volume / Issue` field can store the location. If it's a class lecture, `Publisher / Journal` could be the course name and `Volume / Issue` the university.

> [!cite]
> **Bibliographic Information**
> - **Source Type**:: Lecture
> - **Title**:: How AI could empower any business
> - **Author(s)**:: Ng, Andrew
> - **Year**:: 2023-04-17
> - **Publisher / Journal**:: TED2023
> - **Volume / Issue**:: Vancouver, BC, Canada
> - **Page(s)**:: 00:08:30
> - **URL / DOI**:: `https://www.ted.com/talks/andrew_ng_how_ai_could_empower_any_business`
> - **Date Accessed**:: 2025-10-27

---

## 💬 10. Social Media Post

For sources like X (Twitter), Reddit, LinkedIn, etc. The `Title` field can be the first 20 words of the post. The `Author(s)` should include their name and handle. `Publisher / Journal` is the platform name.

> [!cite]
> **Bibliographic Information**
> - **Source Type**:: Social Media Post
> - **Title**:: We're committing Twitter to help increase the collective health, openness, and civility of public conversation...
> - **Author(s)**:: Dorsey, Jack [@jack]
> - **Year**:: 2018-03-01
> - **Publisher / Journal**:: X (Twitter)
> - **Volume / Issue**:: 
> - **Page(s)**:: 
> - **URL / DOI**:: `https://twitter.com/jack/status/969234275420655616`
> - **Date Accessed**:: 2025-10-27

---

## 🤝 11. Personal Interview / Communication

This is for information you obtained directly from a source that is not published (e.g., an email, a phone call, or a private interview you conducted). This source is typically not recoverable by others, so the `Publisher / Journal` field clarifies the context.

> [!cite]
> **Bibliographic Information**
> - **Source Type**:: Personal Interview
> - **Title**:: Discussion on Obsidian Plugin Development
> - **Author(s)**:: Smith, Jane (Interviewee)
> - **Year**:: 2025-10-20
> - **Publisher / Journal**:: Personal communication with [Your Name]
> - **Volume / Issue**:: Email
> - **Page(s)**:: 
> - **URL / DOI**:: 
> - **Date Accessed**:: 

---

```



