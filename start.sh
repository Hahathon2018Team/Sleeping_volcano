rm -rf current_dataset/
cp -R --attributes-only extracted_dataset/  current_dataset/
python main.py &
python script.py
wait