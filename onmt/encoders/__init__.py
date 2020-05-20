"""Module defining encoders."""
from onmt.encoders.encoder import EncoderBase
from onmt.encoders.transformer import TransformerEncoder
from onmt.encoders.rnn_encoder import RNNEncoder, HREncoder, SeqHREncoder, TGEncoder
from onmt.encoders.cnn_encoder import CNNEncoder
from onmt.encoders.mean_encoder import MeanEncoder

__all__ = ["EncoderBase", "TransformerEncoder", "RNNEncoder", "HREncoder", "SeqHREncoder", "TGEncoder", "CNNEncoder",
           "MeanEncoder"]