- 文本:
	- 加粗文本:

		**加粗文本的一个方式**
		__加粗文本的另一个方式__

	- 斜体文本：

		*斜体文本的方式*
		_斜体文本的另一个方式_

	- 行内代码：

		添加一个`print(hello world)`的行内代码

- 链接：
	1. `[link_name](link "title")`
		这种方式会只显示方括号的里的link_name,鼠标停留在link_name时会显示title

	2. `<link or email>`
		这种方式会显示一个完整的 link 或者 email 在页面

	3. 
		```
		[name][tagger]
		[tagger]: link 'title'

		or 

		[name][]
		[name]: link 'title'
		```
		tagger可以是字母，数字，空白或者标点符号，不区分大小写，也可以忽略，使用name作为tagger

- 标题:

	- # 一级标题
	- ## 二级标题 ##
	- ### 三级标题

- 嵌套段落

	使用>形成一个镶嵌

	```
	这里是一个正常的段落

	> 这里是第一个镶嵌.

	>> 这里是第二个镶嵌

	> 回到第一个镶嵌.

	当我们开始一个新段落或分开不同的双引号时，请注意空格。
	```

- 图片处理
	
	1. 想在这里 ![name](path)插入某个图片

	2. 想在这里 ![name](path 'title')插入鼠标停留会显示title的图片

	3. 有点类似链接的用法：
		```
		![name][tagger]
		[tagger]: path "title"

		or 

		![name][]
		[name]: path "title" height=??px width=??px

		``` 

	4. ??在图片下显示一个标题
		```
		When an image is placed in a paragraph by itself, it is wrapped in a <figure> tag.

		![图片下显示的标题填写在这里][tagger]

		[tagger]: path "This is where the title goes" height=45px width=120px
		```

- 表格：

	1. 一个简单的表格：

	| 第一个标题 | 第二个标题 | 第三个标题 |  
	| :----------- | :-----------: | ------------: |  
	| 左边有一个冒号表示左对齐 | 两边都有冒号表示居中 | 右边有一个冒号表示右对齐 |  
	| Second row   |    **Cell**   |               *Cell* |  

	2. ？一个略微复杂的表格：

	|              | Grouping                    ||  
	| First Header | Second Header | Third Header |  
	| ------------ | :-----------: | -----------: |  
	| Content      | *Long Cell*                 ||  
	| Content      | **Cell**      | Cell         |  
	| New section  | More          | Data         |  

	3. 表格说明：
		- To indicate that a cell should span multiple columns, there simply add additional pipes (|) at the end of the cell, as shown in the example. If the cell in question is at the end of the row, then of course that means that pipes are not optional at the end of that row....

		- Captions are optional, but if present must be at the beginning of the line immediately preceding or following the table, start with [, and end with ]. If you have a caption before and after the table, only the first match will be used.

		- If you have a caption, you can also have a label, allowing you to create anchors pointing to the table. If there is no label, then the caption acts as the label

		- If there is no header for the first column, then cells in that column will be treated as headers, and formatted as such.

		- You can create multiple <tbody> tags within a table by having a single empty line between rows of the table. This allows your CSS to place horizontal borders to emphasize different sections of the table.

- 脚注：
	
	我想在这里添加一个脚注[^firstfootnote]给大家看看， 还想在这里也添加一个[^secondfootnote]给大伙看看

[^firstgootnote]: 这里是为第一个脚注添加的说明
[^secondfootnote]: 这里是为第二个脚注添加的说明



