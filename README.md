# mccolor
Control Minecraft-formatted colored texts in Python

```python
from mccolor import mcwrite

mcwrite('§aThis is green &fand &cthis is red!')
```


```python
from mccolor import mcreplace

text = mcreplace('§aThis is green &fand &cthis is red!')
print(text)
```

```python
from mccolor import mcremove

text = mcremove('§aThis is green &fand &cthis is red!')
print(text)
```
