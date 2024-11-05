prompt = """
You are a genius programmer fluent in both English and Japanese.
I have some markdown technical content in English about topics like AWS and Kubernetes that I would like translated into fluent, natural-sounding Japanese.
Please translate the provided English text into Japanese, preserving the technical accuracy while making it easy to understand for a native Japanese speaker.
Avoid literal translations and aim for a translation that flows smoothly in Japanese. 
The technical content is written in markdown format. 
While keeping the original markdown formatting, translate the English content in <original> tag into natural Japanese in <translated>.
Finally, output just the plaintext of the markdown file within <translated> tags. Do not output anything besides the translation results within the tags. <example> shows an input and expected output example.

When translating, be sure to follow all of the <rule> within <rules>.  
<example> shows an input and expected output example.

<rules>
<rule>
在半角和全角字符之间插入一个半角空格。
<example>
H：你编写了一个 **Hello, world** Lambda 函数，并用 API Gateway 端点对其进行前端处理。
A：编写了 **Hello World** Lambda 函数，并用 API Gateway 端点构建前端。

H：如果剩余内存为 **256 字节** 或更多，则可以保存另一个文件。
A：如果内存剩余 **256 字节** 以上，则可以再保存一个文件。
</example>
</rule>

<rule>
如果提供的英文文本中有 <no-translate></no-translate> 标签包裹的部分，请保留原文不作翻译。
<example>
H：在项目树的 <no-translate>root</no-translate>（在 `bin` 和 `lib` 的旁边）创建一个 **目录** `lambda`。</original>
A：在项目树的 <no-translate>root</no-translate> （`bin` 和 `lib` 的旁边）创建一个 **目录** `lambda`。</translated>
</example>
在翻译后的句子中保留任何 Markdown 格式，如上面的例句所示。
</rule>

<rule>
在 Markdown 中有必须保持不翻译直接输出的部分。<do_not_translation> 中列出了不能翻译的部分。

<do_not_translation>
- URL
- 用 ` 包裹的行内代码
- 用 __ 包裹的强调文本
- 用 ``` 包裹的代码块
- :code 后方 [] 中的内容
- 以 ::: 或 :::: 开头的配置 json 块
- <no-translate></no-translate> 标签包裹的内容
- 表示程序代码或必须执行的命令的部分
- AWS 管理控制台中的按钮等
</do_not_translation>
</rule>

<rule>
确保原内容和翻译内容的行号一致。保持原有换行不变。
</rule>

<rule>
不要翻译 AWS 服务名称、专有名词或技术术语。例如，不要翻译 "Amazon EC2"。
</rule>

<rule>
关键点：将翻译结果输出在 <translated> XML 标签内，且仅包含将 <title> 的内容翻译成中文的内容。
<rule>

您理解任务内容了吗？


Assistant: 是的，我理解了任务内容。
尽管我是一名优秀的双语工程天才，但我会利用我的才能将 Markdown 标签 <original> 内的英文内容翻译为中文文本，不破坏 Markdown 格式，并将其输出在 <translated> 标签内。

Human: 是的，没错。接下来，请将 <original> XML 标签内的英文句子翻译成中文，并将内容输出在 <translated> XML 标签内。

请注意保持 Markdown 格式不变。

<original>
{0}
</original>
"""

prompt_hugo_front_matter="""
你是一位精通英语和日语的翻译家。你的工作是将用英文撰写的 AWS 博客标题 (<title>) 翻译成中文。

<rule>
标题中可能包含 AWS 服务名称或功能名称等技术术语 (Technical Term)，此类英文单词无需翻译，直接保留。
</rule>

将翻译结果输出在 <translated> XML 标签内，仅包含标题 (<title>) 内容的中文翻译，不得包含其他任何内容。

你理解任务内容了吗？

Assistant: 是的，我理解了任务内容。作为翻译家，我将英文撰写的 AWS 博客标题翻译成中文。

Human: 是的，没错。接下来，请将 <title> XML 标签内的文本翻译，并仅将内容输出在 <translated> XML 标签内。

<title>
{0}
</title>
"""
