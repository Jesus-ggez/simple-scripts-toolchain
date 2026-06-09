clear && ls

# bash
#alias tls="clear && tree -a -C -I \".venv|.git|node_modules|target\" -L 3"
#alias tlss="clear && tree -a -C -I \".venv|.git|node_modules!target\""
alias tlsss="clear && tree -a -C -I \".venv|.git|node_modules|target|.env|.gitignore\""
alias tlss="clear && tree -a -C -I \".venv|.git|node_modules|target\""
alias tls="tlss -L 3"

alias clss="clear && ls -a --ignore='__init__.py'"
alias cls="clear && ls --ignore='__init__.py'"

alias update="pkg update && pkg upgrade"

alias alpine="proot-distro login alpine"
alias kill_proc="kill -9 PID"

alias tool="vim ~/.bashrc"
alias viconf="vim ~/.vim/"

alias pkgls="pkg list-installed"
alias pkgu="pkg uninstall"
alias search="pkg search"
alias ins="pkg install"

alias re="exec bash"
alias del="rm -rf"

alias xx="exit"

alias "....."="cd ../../../.."
alias "...."="cd ../../.."
alias "..."="cd ../.."
alias ".."="cd .."


# golang
alias gols="go run main.go"


# java
alias javrun="./mvnw spring-boot:run"


# toolchain
# alias ="python ~/.toolchain/"
alias tc="cd ~/.toolchain"

alias pyinibackend="python ~/.toolchain/py_backend.py"
alias tslitcomp="python ~/.toolchain/ts_pkg_lit_component.py"
alias tsini="python ~/.toolchain/ts_init.py"

alias mkpyrouter="python ~/.toolchain/py_pkg_router.py"
alias mkpymod="python ~/.toolchain/py_module_init.py"

# toolchain.scripts
# alias ="python ~/.toolchain/scripts/"
alias countlines="python ~/.toolchain/scripts/countlines.py"
alias pytermux="python ~/.toolchain/scripts/pytermux.py"
alias delpy="python ~/.toolchain/scripts/delpy.py"


# git
alias pregh="git init && git remote add origin"
alias ingh="git add . && git commit -m"
alias togh="git push -u origin"
alias topr="git push origin"
alias ghnew="git checkout -b"

# python
alias testpy="pytest -v --color=yes --code-highlight=yes"
alias active="source ./.venv/bin/activate"
alias frun="uvicorn main:app --reload"
alias _pyapi="python3 -m http.server"
alias pinr="pip install -r req.txt"
alias pyls="cls && python main.py"
alias pycheck="pyrefly check"
alias nenv="python3.11 -m venv .venv"
alias pyrun="python main.py"
alias pyapp="python app.py"
alias pun="pip uninstall"
alias pin="pip install"
alias pls="pip list"

# uv
#alias uvpyls="cls && uv run"
#alias uvpin="uv add "


# javascript
alias jsrun="npm run dev -- --host 0.0.0.0"
alias jsnew="npm create vite@latest"
#alias astro="npm create astro@latest"
alias npi="npm install"

# rust
alias cpatchelf="patchelf --set-rpath ./"
alias rsbldrel="cargo build --release"
alias tolib="cls && maturin develop"
alias rstest="cargo test"
alias rsbld="cargo build"
alias rschk="cargo check"
alias rsrun="cargo run"
alias rsnew="cargo new"

# postgresql
alias pgini="python ~/.toolchain/scripts/pg_init.py"


export ANDROID_API_LEVEL=$(getprop ro.build.version.sdk)
export PATH=$HOME/.cargo/bin:$PATH
