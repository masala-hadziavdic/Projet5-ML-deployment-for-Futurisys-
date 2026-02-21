from prediction_service import save_prediction_request

def test_insert_request():
    request_id = save_prediction_request(40, 2000, "IT")
    
    assert request_id is not None
    assert isinstance(request_id, int)
    assert request_id > 0