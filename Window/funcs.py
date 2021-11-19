import librosa
import numpy as np
from tensorflow.keras.models import load_model
import tensorflow as tf



def result(features: list) -> list:

    model = load_model('../model/note_predictor.h5')    
    feature = []
    
    for elem in features:
        X, sample_rate = librosa.load(f'../buff_input/{elem}', res_type='kaiser_fast')
        mels = np.mean(librosa.feature.melspectrogram(y=X, sr=sample_rate).T, axis=0)
        feature.append(mels)
        
    feature = np.array(feature).reshape(-1, 16, 8, 1)
    result = np.argmax(model.predict(feature), axis=1)
    result = [x-1 if x != 1 else 7 for x in result]
    return result