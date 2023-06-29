import argparse
from typing import Any
import torchaudio
import torch
import os
from opts import add_decoder_args, add_inference_args
from shutil import rmtree
from nemo.collections.asr.models.rnnt_bpe_models import EncDecRNNTBPEModel
import csv
import torchaudio.transforms as transforms
from torchvision.transforms.functional import resize
import numpy as np
import os
import nemo.collections.asr as nemo_asr
import nemo.collections.nlp as nemo_nlp
import nemo.collections.tts as nemo_tts
import librosa

import tokenizers

from nemo.collections.common.tokenizers.sentencepiece_tokenizer import create_spt_model
from nemo.utils.data_utils import DataStoreObject

class ASRTranscription:
    def __init__(self):
        self.audio_file = ''
        self.hook_layers_output_path = os.path.dirname(__file__).replace("\\", "/")
        self.rnn = []
        self.conv = torch.tensor([])
        self.out = torch.tensor([])
        self.enc_output = torch.tensor([])
        self.dec_out = None  # Initialize the dec_out attribute
        self.flag = -1

    def store_output(self, tensor, dump_folder):
        self.flag += 1
        os.makedirs(dump_folder, exist_ok=True)
        fname = len(os.listdir(dump_folder))
        torch.save(tensor, os.path.join(dump_folder, f"{fname}.pt"))

        if self.flag == 0:
            self.enc_output = tensor
        elif self.flag in [1, 2, 3, 4, 5]:
            self.rnn.append(tensor)
        elif self.flag == 6:
            self.conv = tensor
        elif self.flag == 7:
            self.out = tensor

    def intermediate_hook(self, dump_folder):
        def hook(module, input, output):
            self.store_output(output.detach().cpu().transpose(1, 2), dump_folder)
            print(output.detach().cpu().transpose(1, 2).shape) 
        return hook

    def process_audio_file(self):
        waveform_torchaudio, sample_rate_torchaudio = torchaudio.load(self.audio_file)
        audio_signal_librosa, sample_rate_librosa = librosa.load(self.audio_file, sr=None)

        transform = transforms.MelSpectrogram(sample_rate=sample_rate_torchaudio,n_fft=2048,hop_length=512,	n_mels=161)
        spectrogram = transform(waveform_torchaudio)
        spectrogram_db = torchaudio.transforms.AmplitudeToDB()(spectrogram)

        global resized_spectrogram
        resized_spectrogram = resize(spectrogram_db, (161, 980))
        resized_spectrogram=resized_spectrogram.unsqueeze(0)
        resized_spectrogram=torch.tensor(resized_spectrogram, requires_grad=True)

        inputs=resized_spectrogram

        values = np.random.rand(1, 1, 161, 980)
        tensor = torch.Tensor(values)
        tensor.requires_grad=True
        print(tensor)
        inputs=tensor
        ###############################################################
 


        wav = waveform_torchaudio.mean(dim=0)
        wav = wav.unsqueeze(0)
        wav_len = torch.tensor(len(wav[0])).unsqueeze(0)

        empty_tensor = torch.tensor([])

        
        for f in range(len(asr_model.encoder.layers) - 1):
            if f == 5:
                break
            asr_model.encoder.layers[f].register_forward_hook(
                self.intermediate_hook(os.path.join(self.hook_layers_output_path, f"b{f}"))
            )

        asr_model.encoder.pre_encode.conv.register_forward_hook(
            self.intermediate_hook(os.path.join(self.hook_layers_output_path, "conv"))
        )

        asr_model.encoder.pre_encode.out.register_forward_hook(
            self.intermediate_hook(os.path.join(self.hook_layers_output_path, "out"))
        )

        last_dumpdir = os.path.join(self.hook_layers_output_path, "enco")
        
 

        with torch.no_grad():
            processed, processed_len = asr_model.preprocessor(input_signal=wav, length=wav_len)
            enc_out = asr_model.encoder(audio_signal=processed, length=processed_len)[0].detach().cpu()
            #####
            asr_model.decoder.register_forward_hook(self.intermediate_hook(os.path.join(self.hook_layers_output_path, "dec_out")))
             
            self.dec_out = asr_model.decoder(encoder_output=enc_out)


            '''
            TypeError: Input argument preprocessed_signal has no corresponding input_type match. Existing input_types = dict_keys(['input_signal', 'input_signal_length', 'processed_signal', 'processed_signal_length', 'sample_id'])
            '''
            # Perform inference
            logits, _ = asr_model(processed_signal=processed)



        # self.store_output(enc_out, last_dumpdir)
        # print('# ', '*'*30 ,'dec_out)', dec_out)
        # print('# ', '*'*30 ,'dec_out.shape)', dec_out.shape)
        # self.store_output(dec_out, last_dumpdir)
         
        # print("below are the encoder output")
        # print(self.enc_output)

        subsampling_factor = getattr(asr_model.encoder.pre_encode, 'subsample_factor', 4)
        encoder_output_lengths = torch.ceil(wav_len.float() / subsampling_factor).int()
        output_sizes = encoder_output_lengths // subsampling_factor

        global output_sizes_forward
        output_sizes_forward = output_sizes.detach()
        output_sizes_forward = output_sizes.float().requires_grad_()
        # print("Output Sizes:", output_sizes)

        # print("below are the rnn")
        # print(len(self.rnn))
        global rnn_0_forward, rnn_1_forward, rnn_2_forward, rnn_3_forward, rnn_4_forward
        rnn_0_forward = self.rnn[0].float().requires_grad_()
        rnn_1_forward = self.rnn[1].float().requires_grad_()
        rnn_2_forward = self.rnn[2].float().requires_grad_()
        rnn_3_forward = self.rnn[3].float().requires_grad_()
        rnn_4_forward = self.rnn[4].float().requires_grad_()

        # print("below are the conv")
        global conv_forward
        conv_forward = self.conv.float().requires_grad_()
        # print(conv_forward)

        # print("below are the out")
        global out_forward
        out_forward = self.out.float().requires_grad_()
        # print(out_forward)

        # print("below are the dec_out")
        global dec_out_forward
        dec_out_forward = self.dec_out.float().requires_grad_()
        # print('# ','*'*30,'dec_out_forward',dec_out_forward)
        # print('# ','*'*30,'dec_out_forward',dec_out_forward.shape)
        # print('# ','*'*30,model.decoder.register_forward_hook)
        print('# ', '*'*30 ,'dec_out_forward)', dec_out_forward)
        print('# ', '*'*30 ,'dec_out_forward.shape)', dec_out_forward.shape)



        '''
        # This line is to use the stt_de_conformer_transducer_large Language Model from Nvidia:
        
        from nemo.collections.asr.models.rnnt_bpe_models import EncDecRNNTBPEModel

        model = EncDecRNNTBPEModel.from_pretrained(model_name="stt_de_conformer_transducer_large")
        model.decoder


        # ####################################################

        # Acoustic model
        import nemo.collections.asr as nemo_asr

        asr_model = nemo_asr.models.EncDecRNNTBPEModel.from_pretrained(model_name="stt_de_conformer_transducer_large")

        '''

        print('********************** Done! ***********************')



if __name__ == '__main__':
    main_path='/home/mmm2050/QU_DFKI_Thesis/Experimentation/ASR_Accent_Analysis_De'
    parser = argparse.ArgumentParser(description='DeepSpeech transcription')
    parser = add_inference_args(parser)
    parser.add_argument('--test_manifest', metavar='DIR',help='path to validation manifest csv', default=main_path+'/DeepSpeech/data/test_manifest_De_small.csv')
    parser = add_decoder_args(parser)
    args = parser.parse_args()

    asr_model = nemo_asr.models.EncDecCTCModelBPE.from_pretrained("stt_de_conformer_ctc_large")
     # using the asr nemo lang model 
    # model = EncDecRNNTBPEModel.from_pretrained(model_name="stt_de_conformer_transducer_large")
    # model.decoder


    AAA=[]
    
    asr_transcription = ASRTranscription()
    # Enter the path to the audio file (WAV format)

    # Read the CSV file
    with open(args.test_manifest, "r") as csv_file:
        csv_reader = csv.reader(csv_file)
        
        # Iterate over each row in the CSV
        for row in csv_reader:
            audio_path = row[0]  # Get the audio path from the first column
            
            # Extract the directory path without the file name and extension
            audio_dir_path = os.path.dirname(audio_path)
            
            # Append the directory path to the RRR list
            AAA.append(audio_dir_path)


  

 

    #######################################################################################
    # # Load the ASR model and tokenizer

    # #tokenizer = load_tokenizer()
    # # tokenizer = asr_model.make_vocab()
    # tokenizer = asr_model.tokenizer
    # # Preprocess the encoder output (e.g., reshape tensors)
    # preprocessed_output = preprocess_encoder_output(encoder_output)

    # # Decode the encoder output
    # decoded_tokens = asr_model.decode(preprocessed_output)

    # # Convert tokens to characters using the tokenizer
    # transcription = tokenizer.convert_tokens_to_string(decoded_tokens)

    # # Print the final transcription
    # print(transcription)
    ############################################################################################




  
    asr_transcription.audio_file = AAA[0]+'/common_voice_de_17347675.wav'

    asr_transcription.process_audio_file()


    # waveform_torchaudio, sample_rate = torchaudio.load(self.audio_file)
    # audio_signal_librosa, sample_rate = librosa.load(self.audio_file, sr=None)
    print('waveform_torchaudio',waveform_torchaudio)


    tokenizer = asr_model.tokenizer(waveform_torchaudio)
    
    print('*'*30,' Done!','*'*30)