# deep-learning-with-keras

## Installation

### Ubuntu 혹은 Windows 10 + WSL 사용자 (필수)

```
$ sudo apt update

// sudo apt update error: "Release file is not yet valid" 오류 발생시:
$ sudo hwclock --hctosys

$ sudo apt upgrade
$ sudo apt install -y build-essential libncurses5-dev libffi-dev libbz2-dev zlib1g zlib1g-dev libreadline-dev libsqlite3-dev
```

### pyenv 설치

```
$ brew install pyenv
$ brew install pyenv-virtualenv
```

### python 설치

```
$ pyenv install --list
$ pyenv install 3.7.11
$ pyenv versions
```

### ~/.profile 업데이트

```
...

export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/shims:$PATH"

if which pyenv > /dev/null; then eval "$(pyenv init -)"; fi
if which pyenv-virtualenv-init > /dev/null; then eval "$(pyenv virtualenv-init -)"; fi
```

### poetry 설치

```
$ brew install poetry
```

## Manage Project

### venv 생성

```
$ poetry config virtualenvs.in-project true
$ poetry config virtualenvs.path "./.venv"

# 프로젝트 내부에 venv 새로 설치
$ pyenv local 3.7.11
$ poetry install && poetry update
```

---

## References

- [Poetry](https://python-poetry.org/docs/cli/)
- [Black - The uncompromising code formatter](https://github.com/psf/black)
- [[Python] poetry를 사용하는 프로젝트를 vscode에서 개발할 때 interpreter를 잡는 방법](https://amazingguni.medium.com/python-poetry를-사용하는-프로젝트를-vscode에서-개발할-때-interpreter를-잡는-방법-e1806f093e6d)
