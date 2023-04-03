:set shiftwidth=4
:set tabstop=4
:set softtabstop=4
:set autoindent
:set mouse=a
:set number relativenumber
syntax on

" disable arrow-keys
no <Up> <Nop>
no <Down> <Nop>
no <Left> <Nop>
no <Right> <Nop>
ino <Up> <Nop>
ino <Down> <Nop>
ino <Left> <Nop>
ino <Right> <Nop>

" char autoclose
":inoremap ( ()<Esc>i
":inoremap [ []<Esc>i
":inoremap { {}<Esc>i
":inoremap < <><Esc>i
":inoremap " ""<Esc>i
":inoremap ' ''<Esc>i
":inoremap ` ``<Esc>i
