# flash card

#### google sheet   for translate each of cell  

`=GOOGLETRANSLATE("Hello World","en","es")`


# note pandas

```python
dataframe = pd.read_csv(file)
data = dataframe.to_dict(orient="records")

data_to_learn = pandas.DataFrame(data)
data_to_learn.to_csv("./data/french_english_to_learn.csv")
```

# tkinter  use  after and aafter_cansel  for handling delay
##  `tk.after(milisecond,nameFunction)`
```python
flip_timer = tk.after(3000, back_card)
tk.after_cancel( flip_timer)  # for each time run function separately counted timer
```
       
# reconfig
reconfig
`canvas.itemconfig(word,text="")`
`word=canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))`

# PhotoImage class ✅
PhotoImage objects should not be created inside a function. Otherwise, it will not work.

