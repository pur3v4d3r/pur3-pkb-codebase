@echo off
echo =============================================
echo Book Formatting Agent: The Fellowship of the Ring
echo =============================================
echo.
echo Input:  _tmp_fellowship_raw.md
echo Output: _tmp_book_fellowship.md
echo.
echo Starting formatting process...
echo.

python "D:\10_pur3v4d3r's-vault\_scripts\format_fellowship.py"

echo.
if %ERRORLEVEL% == 0 (
    echo SUCCESS: Formatting complete!
    echo Output written to: D:\10_pur3v4d3r's-vault\_tmp_book_fellowship.md
) else (
    echo ERROR: Script failed with error code %ERRORLEVEL%
)

echo.
pause
