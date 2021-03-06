# python-template

## Installation

### Ubuntu 혹은 Windows 10 + WSL 사용자 (필수)

```
$ sudo apt update

// sudo apt update error: "Release file is not yet valid" 오류 발생시:
$ sudo hwclock --hctosys

$ sudo apt upgrade
$ sudo apt install -y build-essential
$ sudo apt install -y libncurses5-dev libffi-dev libbz2-dev zlib1g zlib1g-dev libreadline-dev libsqlite3-dev
$ sudo apt install -y python3-tk tk-dev
```

### pyenv 설치

```
$ brew install pyenv
$ brew install pyenv-virtualenv
```

### python 설치

```
$ pyenv install --list

# for tkinter (before installing pyhton)
$ export LDFLAGS="-L/usr/local/opt/tcl-tk/lib"
$ export CPPFLAGS="-I/usr/local/opt/tcl-tk/include"
$ export PATH=$PATH:/usr/local/opt/tcl-tk/bin

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
$ poetry config --list

# 프로젝트 내부에 venv 새로 설치
$ pyenv local 3.7.11
$ poetry install && poetry update
```

### 패키지 이름 변경

1. `changeme/` 디렉터리를 새 패키지 이름으로 바꿉니다.

   ```
   $ mv changeme <new_package_name>
   ```

1. `pyproject.toml` 파일을 수정합니다.

   ```
   [tool.poetry]
   name = "<new_package_name>"
   ```

1. 프로젝트를 refresh 합니다.

   ```
   $ poetry install && poetry update
   ```

---

## References

- [Poetry](https://python-poetry.org/docs/cli/)
- [[Gist] Python Poetry Cheatsheet](https://gist.github.com/CarlosDomingues/b88df15749af23a463148bd2c2b9b3fb)
- [Black - The uncompromising code formatter](https://github.com/psf/black)
- [[Python] poetry를 사용하는 프로젝트를 vscode에서 개발할 때 interpreter를 잡는 방법](https://amazingguni.medium.com/python-poetry를-사용하는-프로젝트를-vscode에서-개발할-때-interpreter를-잡는-방법-e1806f093e6d)
- [WSL2에서 X window를 세팅하는 법](https://evandde.github.io/wsl2-x/)
- [Python not configured for Tk](https://newbedev.com/python-not-configured-for-tk)
