:set shiftwidth=4
:set tabstop=4
:set softtabstop=4
:set autoindent
:set mouse=a
:set number
syntax on

call plug#begin()

Plug 'https://github.com/dracula/vim'
Plug 'scrooloose/nerdtree'
Plug 'https://github.com/vim-airline/vim-airline'
Plug 'https://github.com/neoclide/coc.nvim'

call plug#end()

" shortcuts
:nnoremap <C-q> :NERDTreeFocus<cr>
:nnoremap <C-w> :NERDTree<cr>
