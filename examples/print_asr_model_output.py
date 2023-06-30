# Acoustic model
import nemo.collections.asr as nemo_asr
asr_model = nemo_asr.models.EncDecRNNTBPEModel.from_pretrained(model_name="stt_de_conformer_transducer_large")


# Linguastic model
from nemo.collections.asr.models.rnnt_bpe_models import EncDecRNNTBPEModel
model = EncDecRNNTBPEModel.from_pretrained(model_name="stt_de_conformer_transducer_large")
model.decoder


print('***'*60)
print(asr_model)
print('***'*60)