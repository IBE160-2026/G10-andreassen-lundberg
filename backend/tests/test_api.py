def test_health_reports_rule_based_explainer_by_default(client):
    response = client.get("/api/health")

    assert response.status_code == 200
    assert response.json()["explainer"] == "regelbasert"


def test_list_datasets(client):
    response = client.get("/api/datasets")

    assert response.status_code == 200
    assert [d["id"] for d in response.json()] == ["test"]


def test_unknown_dataset_gives_404(client):
    assert client.get("/api/datasets/finnes-ikke").status_code == 404
