rm -rf current_dataset/
cp -R --attributes-only extracted_dataset/  current_dataset/
python3 main.py &
python3 script.py
wait