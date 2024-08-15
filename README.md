# 谐音梗检测器 v1.0
<p>中文&nbsp ｜ &nbsp<a href="README_EN.md">English</a>&nbsp</p>
基于成语数据库检测可能的谐音成语，并利用大语言模型的能力加以解释。

## 简介
建立新华字典的成语集合的数据集。<br>
特别感谢 [pwxcoo/chinese-xinhua](https://github.com/pwxcoo/chinese-xinhua) 的成语集合文件！<br>
基于用户输入的人名与关键字，自动搜索可能的谐音结果。<br>

## 使用
人名：谐音的人名主体。<br>
关键字：谐音的关键字主体。<br>
严格模式：是否严格检测声调。若为是，则只返回声调严格相同之结果。若为否，则拼音相同即返回结果。<br>

![使用界面](assets/intro.png)