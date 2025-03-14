"""
Pretrained AI model based on 
distilbert/distilgpt2 AI model
Uses: 
Creative Writing and Art
"""
from transformers import GPT2Tokenizer, GPT2Model
from datasets import load_dataset

tokenizer = GPT2Tokenizer.from_pretrained('distilgpt2')
model = GPT2Model.from_pretrained('distilgpt2')

def tokenize_function(examples):
  return tokenizer(examples["text"])
