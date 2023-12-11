
# Outline Key Manager

A simple key management manager for Outline VPN.

Based on [outline-vpn-api](https://pypi.org/project/outline-vpn-api/).


## Usage/Examples

Import library:
```python
import outline_key_manager as okm
```

---

Initialize Outline using your API key:
```python
okm.init("https://x.x.x.x:xxxxx/xxxxxxxxxxxxxxxxxxxxx", debug=True) # -> str
```

---

If you want, you can use Config_Reader for this:
```python
okm.init(config.outline_api.get_secret_value(), debug=True) # -> str
```
Your .env file:
```env
OUTLINE_API=https://x.x.x.x:xxxxx/xxxxxxxxxxxxxxxxxxxxx
```

---

Get all your keys:
```python
okm.get_all_keys() # -> str
```

---

Create a new key:
```python
okm.new_key(name="Example1") # -> int
```

---

Get information about key:
```python
okm.get_key("Example1") # -> str | int
```

---

Rename from Example1 to NewExampleName:
```python
okm.rename_key("Example1", "NewExampleName") # -> int
```

---

Set limit to 2GB:
```python
okm.set_limit("NewExampleName", 2048) # -> int
```

---

Remove limit:
```python
okm.remove_limit("NewExampleName") # -> int
```

---

Remove key:
```python
okm.remove_key("NewExampleName") # -> int
```

## Exit codes:
[Xelond Exit Codes](https://exitcode.ru/)
## Used By

This project is used by the following companies:

- [SlyFox VPN](https://slyfoxvpn.ru/) (coming soon)
## Authors

- [@xelond-dev](https://www.github.com/xelond-dev)

If you have questions or personal suggestions, use my telegram - [@xelond](https://t.me/xelond)
