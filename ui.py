import gradio as gr

from funcs import search, explain_homophone

def demo():
    with gr.Blocks() as demo:
        gr.HTML("<h1 style='font-size: 30px;'>谐音成语检测器 v1.0</h1>")
        gr.HTML("<p style='font-size: 20px;'>检测可能存在的谐音成语, made by 肥桥今天吃什么@bilibili</p>")

        with gr.Column():
            name = gr.Textbox(
                placeholder="人名，如'宫崎'", 
                label="人名谐音部分",
                elem_id="name"
            )
            full_name = gr.Textbox(
                placeholder="全名，如'宫崎英高'", 
                label="人名全名（选填）",
                elem_id="full_name"
            )
            keyword = gr.Textbox(
                placeholder="谐音关键字，如'神坛'", 
                label="关键字",
                elem_id="keyword"
            )
            full_keyword = gr.Textbox(
                placeholder="整体关键字，如'跌落神坛'", 
                label="整体关键字（选填）",
                elem_id="full_keyword"
            )
            is_strict = gr.Checkbox(
                label="严格模式（声调必须严格相同）", 
                elem_id="is_strict", 
                value=True
            )
            submit_button = gr.Button(
                value="寻找谐音！",
                interactive=False,
            )
            explain = gr.Textbox(
                label="谐音解释", 
                lines=5,
                elem_id="explain"
            )

            # submit button只有在name和keyword都有输入时才会激活
            def update_button_state(name, keyword):
                interactive = bool(name and keyword)
                return gr.update(interactive=interactive)
            
            # Button interactive logic
            name.change(update_button_state, inputs=[name, keyword], outputs=submit_button)
            keyword.change(update_button_state, inputs=[name, keyword], outputs=submit_button)

            @gr.render(inputs=[name, full_name, keyword, full_keyword, is_strict], triggers=[submit_button.click])
            def show_split(name, full_name, keyword, full_keyword, is_strict):
                matches = search(name, full_name, keyword, full_keyword, is_strict)
                if len(matches) == 0:
                    gr.Markdown("## 没有找到匹配的谐音成语")
                with gr.Blocks():
                    for match in matches:
                        with gr.Row():
                            tb_idiom = gr.Textbox(
                                value=match.idiom, 
                                label="原始成语",
                                scale=4
                            )
                            tb_homophone = gr.Textbox(
                                value=match.homophone, 
                                label="谐音成语",
                                scale=4
                            )
                            explain_btn = gr.Button(
                                "解释谐音！",
                                scale=1
                            )
                            name, keyword = match.name, match.keyword
                            def give_explain(idiom, homophone):
                                return explain_homophone(idiom, homophone, name, keyword)
                            explain_btn.click(give_explain, inputs=[tb_idiom, tb_homophone], outputs=[explain])

    return demo

demo().launch(
    debug=True,
)
