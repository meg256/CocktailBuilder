from textgenrnn import textgenrnn
cb = textgenrnn(weights_path='cocktailbuilder_weights.hdf5',
                       vocab_path='cocktailbuilder_vocab.json',
                       config_path='cocktailbuilder_config.json')
 
cb.generate_samples(max_gen_length=200)
cb.generate_to_file('cocktailbuilder_textgenrnn_texts.txt', temperature=1.2, n=20, max_gen_length=200)