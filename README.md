# aichallenge_folktune-VAE
My entry for "The Ai Music Generation Challenge 2022" using folktune-VAE.

The generated tunes are found in `tunes.abc` and the midi files are available in `midis.tar.xz`.

The checkpoint used for sampling is `best_ft.pytorch`. This checkpoint was obtained after fine tuning starting from `best.pytorch`.

To sample,`python3 inference.py -c {checkpoint} -nl 2 -hs 256 -ls 32 -ms 256 -n {number of samples} -m topp -p {p} -t {temperature} -s --seed {seed}`.
To randomize keys, move rename the generated file as `test.abc`, create a `tmp` directory and call `python3 random_key.py > {destination}`.
