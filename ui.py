import gradio as gr

from search import search

def demo():
    with gr.Blocks() as demo:
        gr.HTML("<h1 style='font-size: 30px;'>谐音成语检测器 v1.0</h1>")
        gr.HTML("<p style='font-size: 20px;'>检测可能存在的谐音成语, made by 肥桥今天吃什么@bilibili</p>")

        with gr.Column():
            name = gr.Textbox(
                placeholder="人名的谐音部分", 
                label="人名",
                elem_id="name"
            )
            full_name = gr.Textbox(
                placeholder="人名全名（选填）", 
                label="人名",
                elem_id="full_name"
            )
            keyword = gr.Textbox(
                placeholder="谐音关键字", 
                label="关键字",
                elem_id="keyword"
            )
            full_keyword = gr.Textbox(
                placeholder="关键字全名（选填）", 
                label="关键字",
                elem_id="full_keyword"
            )
            is_strict = gr.Checkbox(
                label="严格模式（严格检测声调）", 
                elem_id="is_strict", 
                value=True
            )
            explain = gr.Textbox(
                label="谐音解释", 
                lines=5,
                elem_id="explain"
            )
            output = gr.Textbox(
                label="全部检测结果", 
                lines=5,
                elem_id="output"
            )

            submit_button = gr.Button(
                value="寻找谐音！",
                interactive=False,
            )

            # submit button只有在name和keyword都有输入时才会激活
            def update_button_state(name, keyword):
                interactive = bool(name and keyword)
                print(f"interactive: {interactive}")
                return gr.update(interactive=interactive)

            # Button interactive logic
            name.change(update_button_state, inputs=[name, keyword], outputs=submit_button)
            keyword.change(update_button_state, inputs=[name, keyword], outputs=submit_button)

            def process(name, full_name, keyword, full_keyword, is_strict):
                output, explain = search(name, full_name, keyword, full_keyword, is_strict)
                return output, explain

            submit_button.click(process, inputs=[name, full_name, keyword, full_keyword, is_strict], outputs=[output, explain])

    return demo

demo().launch(
    debug=True,
)
