Status: not filed (GitHub issues are disabled for iambibhas/GeneratePassword)

# Generate Password: "secure" passwords come from `random`, which is not for security use

Claude reports:

Tested on Sublime Text 4, build 4215, Windows (package 1.1.1, Python 3.14 plugin host). The six commands work (`generate_short_password` ... `generate_long_secure_password`): they replace each selection with a password of 10, 15 or 20 characters.

`password.py` builds the password with `random.sample(population, length)`. The Python documentation for the `random` module says it "should not be used for security purposes" and points to the `secrets` module (or `random.SystemRandom`) instead. For a package whose commands are named "secure password" that matters: the output of a Mersenne Twister generator is predictable once enough output is seen, and it is seeded from the clock/OS only once per process.

Also observed:

- `sample` draws without replacement, so no character repeats within one password (a 20 character password uses 20 different characters out of 82).
- With several cursors, every selection gets the same password (three cursors gave three identical lines).

Fix, tested as a loose copy: use the system generator,

```python
from random import SystemRandom, choice, randrange
_rng = SystemRandom()
...
p = ''.join(_rng.sample(population, self.length))
```

With that change the commands still work and give a 20 character password in each selection.
