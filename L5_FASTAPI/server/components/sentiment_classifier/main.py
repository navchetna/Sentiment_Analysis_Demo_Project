import warnings
from pathlib import Path
import time
from transformers import AutoModelForSequenceClassification, AutoTokenizer
import numpy as np
import openvino as ov
import torch

class TextClassifier:
    def __init__(self, checkpoint, model_dir="my_models/", max_seq_length=128):
        self.checkpoint = checkpoint
        self.model_dir = model_dir
        self.max_seq_length = max_seq_length
        self.model = AutoModelForSequenceClassification.from_pretrained(checkpoint)
        self.tokenizer = AutoTokenizer.from_pretrained(checkpoint)
        self.ir_xml_name = checkpoint + ".xml"
        self.ir_xml_path = Path(self.model_dir) / self.ir_xml_name
        self.input_info = [(ov.PartialShape([1, -1]), ov.Type.i64), (ov.PartialShape([1, -1]), ov.Type.i64)]
        self.default_input = torch.ones(1, max_seq_length, dtype=torch.int64)
        self.inputs = {
            "input_ids": self.default_input,
            "attention_mask": self.default_input,
        }
        self.ov_model = ov.convert_model(self.model, input=self.input_info, example_input=self.inputs)
        ov.save_model(self.ov_model, self.ir_xml_path)
        self.core = ov.Core()
        self.device = 'AUTO'
        self.compiled_model = self.core.compile_model(self.ov_model, self.device)
        self.infer_request = self.compiled_model.create_infer_request()

    def softmax(self, x):
        e_x = np.exp(x - np.max(x))
        res = e_x / e_x.sum()
        return res

    def infer(self, input_text):
        input_text = self.tokenizer(
            input_text,
            truncation=True,
            return_tensors="np",
        )
        inputs = dict(input_text)
        label = {0: "NEGATIVE", 1: "POSITIVE"}
        result = self.infer_request.infer(inputs=inputs)
        for i in result.values():
            probability = np.argmax(self.softmax(i))
        return label[probability]
