# Text Comparison Web Service

This project implements a web service for comparing text similarity using various methods, including Cosine Similarity, Euclidean Distance, Jaccard Similarity and Dynamic Time Warping (DTW) Distance. The service is built using Flask, a lightweight web framework for Python.

## Getting Started

### Prerequisites

- Python 3.x
- Flask

Install the required dependencies using the following command:

```bash
pip install Flask 
```

### Running the Web Service

Run the Flask application using the following command:

```bash
python app.py
```

The web service will be accessible at `http://127.0.0.1:5000/`. Ensure that the service is running before making requests.

## Endpoint

### Text Comparison

- **Endpoint:** `/compare`
- **Method:** POST
- **Payload:** JSON object with the following parameters:
  - `text1`: The first text for comparison
  - `text2`: The second text for comparison
  - `metric`(optional, default=cosine) : The similarity metric to use (`cosine`, `dtw`)
  - `n_gram`(optional, default=2) : No to use for ngrams (only used for jaccard and dtw)

**Response:** JSON object with the result based on the specified metric.

Example Request:
```bash
curl -X POST -H "Content-Type: application/json" -d '{"text1": "Sample text 1", "text2": "Sample text 2", "metric": "jaccard", "n_grams":2}' http://127.0.0.1:5000/compare
```

Supported metrics:
- `cosine` : Cosine Similarity
- `euclidean`: Euclidean Distance
- `jaccard`: Jaccard Similarity
- `dtw`: Dynamic Time Warping Distance

## Authors

- Atharva Wandile

## License

This project is licensed under the [MIT License](LICENSE).
```