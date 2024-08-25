# Homophone Detection Tool v1.0
<p><a href="README.md">中文</a> &nbsp ｜ &nbspEnglish&nbsp</p>
Detect potential homophone idioms based on an idiom database and use the capabilities of large language models to provide explanations.

## Introduction
Establish a dataset of idioms from the Xinhua Dictionary.<br>
Special thanks to pwxcoo/chinese-xinhua for the idiom collection file!<br>
Automatically search for potential homophone results based on user input of names and keywords.<br>

## Usage
Name: The subject of the homophonic name.<br> 
Full Name (Optional): The full name, used for understanding the homophonic part more precisely. This is set up because there might be parts of the full name that should not be included in the homophonic interpretation.<br> 
Keyword: The subject of the homophonic keyword.<br> 
Full Keyword (Optional): The full form of the keyword, following a similar idea to the full name setup.<br> 
Strict Mode: Whether to strictly detect tone. If yes, only results with exactly the same tones will be returned. If no, results with the same pinyin will be returned.<br>

![Interface](assets/intro.png)