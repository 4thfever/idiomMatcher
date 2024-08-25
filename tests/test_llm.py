try:
    from local_llm import call_api
except:
    from llm import call_api

def test_call_api():
    response = call_api("你好")
    assert response is not None