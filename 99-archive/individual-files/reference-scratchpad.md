

**Table of Contents** (*T.O.C.*)

1. [[#Intrusional Characters]]
2. 
3. 
4. 
5. 
6. 
7. 
8. 

---


# Intrusional Characters

>[!the-purpose]
>**Taking out random intrusional character from Reports, from LLM.**

```
1.  Press `Ctrl + Shift + F` (or `Cmd + Shift + F` on Mac) to open **Search across all files**. (Or `Ctrl + F` for just the current file).
2.  Click the icon that looks like `.*` to **Enable Regular Expression**.
3.  In the "Find" field, paste this:
    `\\>`
4.  In the "Replace" field, just type a greater-than sign:
    `>`
5.  Click **"Replace all"**.
```

>[!what-this-does]
>
> * The "Find" command `\\>` is a regex pattern. The first backslash (`\`) escapes the second backslash, so it's literally searching for the *character* `\`.
> * It then finds the `>` that immediately follows it.
> * The "Replace" command replaces that two-character string (`\>`) with the single, correct `>` character.
>
> This will instantly fix every broken callout in your 10,000-word document in less than a second.
>
> I hope this helps you reclaim that lost productivity! Would you like me to help you refine the prompt for your "Gem-Instruction-Set" to be even more robust against this?

















































































































































