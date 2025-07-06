import sys
sys.path.append("../src")
import unittest
from unittest.mock import patch, MagicMock
from Augment_Generation import run_query


class TestRunQuery(unittest.TestCase):

    @patch("your_module_name.HuggingFaceEmbeddings")
    @patch("your_module_name.Chroma")
    @patch("your_module_name.client.chat.completions.create")
    def test_run_query(self, mock_create, mock_chroma, mock_embeddings):
        # Mock docs returned by retriever.invoke()
        mock_doc1 = MagicMock()
        mock_doc1.page_content = "Customer complaint about delay in service."

        mock_retriever = MagicMock()
        mock_retriever.invoke.return_value = [mock_doc1]

        mock_vector_store = MagicMock()
        mock_vector_store.as_retriever.return_value = mock_retriever

        mock_chroma.return_value = mock_vector_store
        mock_embeddings.return_value = MagicMock()

        # Mock OpenAI response
        mock_response = MagicMock()
        mock_response.choices = [MagicMock(message=MagicMock(content="Mocked response"))]
        mock_create.return_value = mock_response

        # Run function
        prompt = "Why was the customer unhappy?"
        result = run_query(prompt)

        # Assert result
        self.assertEqual(result, "Mocked response")
        mock_create.assert_called_once()


if __name__ == '__main__':
    unittest.main()
