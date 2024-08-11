import gradio as gr

from search import search

def demo():
    with gr.Blocks() as demo:
        gr.HTML("<h1 style='font-size: 30px;'>谐音成语检测器 v1.0</h1>")
        gr.HTML("<p style='font-size: 20px;'>检测可能存在的谐音成语, made by 肥桥今天吃什么@bilibili</p>")

        with gr.Column():
            name_input = gr.Textbox(
                placeholder="输入人名,多个间用逗号分隔", 
                label="人名",
                elem_id="name_input"
            )
            keyword_input = gr.Textbox(
                placeholder="输入关键字,多个间用逗号分隔", 
                label="关键字",
                elem_id="keyword_input"
            )
            is_strict = gr.Checkbox(
                label="严格模式", 
                elem_id="is_strict", 
                value=True
            )
            output = gr.Textbox(
                label="检测结果", 
                lines=5,
                elem_id="output"
            )

            def process(name, keyword, is_strict):
                return search(name, keyword, is_strict)

            submit_button = gr.Button("开始谐音！")
            submit_button.click(process, inputs=[name_input, keyword_input, is_strict], outputs=output)

    return demo

demo().launch()
