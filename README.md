# hyperskill-DuplicateFileHandler-python
Duplicate File Handler is a useful tool that can free some space on your drive. Write a handler that checks and compares files in a folder, displays the result, and removes duplicates.  
https://hyperskill.org/projects/176  

<img src="https://github.com/drtierney/hyperskill-DuplicateFileHandler-python/blob/main/duplicate-file-handler.gif"/>

## Syntax
| Arg | Valuelist | Comment
| --- | --------- | ------- |
| path | `<String>` | Required<br>Absolute or relative path to directory|

```
handler.py D:\temp\module
```


```
handler.py ../backups
```

## Stages
**Stage #1: Here come the files**  
Scan files and folders with the help of the OS module.  

**Stage #2: How much does it weigh?**  
Use file sizes to find duplicate files.  

**Stage #3: Whats the hash about?**  
Learn about hash functions and implement them in your code.  

**Stage #1: Delete them all**  
Let's delete all duplicates. 
