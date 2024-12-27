syntax on
set shiftwidth=4
set tabstop=4
set softtabstop=4
set autoindent
" set mouse=
set number relativenumber
" filetype plugin indent on
let  mapleader="\<Space>"

call plug#begin()

Plug 'preservim/nerdtree' " Nerdtree
Plug 'vim-airline/vim-airline' " vim-airline
Plug 'LunarWatcher/auto-pairs' " auto-close braces (this is a maintained fork)
Plug 'tpope/vim-commentary' " Comment lines
Plug 'tpope/vim-surround' " surrounding
Plug 'Vimjas/vim-python-pep8-indent' " python indentation
" Plug 'voldikss/vim-floaterm' " terminal
" Plug 'preservim/tagbar' " tagbar
" Plug 'lifepillar/pgsql.vim' " sql syntax highlight

" live_grep & buffers
Plug 'BurntSushi/ripgrep'
Plug 'nvim-lua/plenary.nvim'
Plug 'nvim-telescope/telescope.nvim', { 'tag': '0.1.8' }

call plug#end()

func! HighlightSQLInPython()
	hi link sqlKeyword String
	" Link Python string highlighting to SQL keywords
	syn match sqlKeyword "\v(SELECT|FROM|WHERE|INSERT|INTO|UPDATE|DELETE|AND|OR|NOT|LIKE|IN|COUNT|AVG|MAX|MIN|INT|VARCHAR|CHAR|TEXT)" containedin=pythonString
	" Ensure that Python strings are highlighted correctly
	hi link sqlKeyword Keyword
endfunc

" Automatically call this function for Python files
autocmd FileType python call HighlightSQLInPython()

" shortcuts
" nnoremap <C-f> :NERDTreeFocus<CR>
" nnoremap <C-n> :NERDTree<CR>
" nnoremap <C-t> :NERDTreeToggle<CR>
noremap <C-c> "+y<CR>
tnoremap <C-t> <C-\><C-n>

nnoremap <C-n> :NERDTreeToggle<CR>
nmap <F9> :TagbarToggle<CR>

" open terminal
nnoremap <Leader>t :split<CR>:terminal<CR>

" save session, write changes and exit
func SaveSession(path)
	NERDTreeClose
	" FloatermKill
	execute "mksession! ~/.config/nvim/sessions/" .. a:path
	xa
endfunc

command! -nargs=1 Xs call SaveSession(<f-args>)


" save/ load/ remove/ list sessions
nnoremap <Leader>ss :Xs 
nnoremap <Leader>os :source ~/.config/nvim/sessions/
nnoremap <Leader>rs :!rm ~/.config/nvim/sessions/
nnoremap <Leader>ls :!ls ~/.config/nvim/sessions/ <CR>

" ranger through floaterm
" func OpenRanger()
" 	:FloatermNew --height=0.6 --width=0.4 --wintype=float --name=filemanager
" 				\ --position=topleft --autoclose=2 ranger --cmd="cd ~"
" endfunc
" command! Ranger call OpenRanger()
"
"
" let g:floaterm_keymap_toggle = '<Leader>t'
" let g:floaterm_wintype = 'split'
" let g:floaterm_height = 0.4		

let NERDTreeShowHidden = 1

" colorscheme
set background=dark

" change color when line reaches max chars (81)
highlight OverLength ctermbg=gray ctermfg=black guibg=#cf7586
match OverLength /\%100v.\+/

" baaammm
no <Up> <Nop>
no <Down> <Nop>
no <Left> <Nop>
no <Right> <Nop>
ino <Up> <Nop>
ino <Down> <Nop>
ino <Left> <Nop>
ino <Right> <Nop>

" Telescope shortcuts
nnoremap <leader>ff <cmd>Telescope find_files<cr>
nnoremap <leader>fg <cmd>Telescope live_grep<cr>
nnoremap <leader>fb <cmd>Telescope buffers<cr>

set list lcs=tab:\|\ 
highlight NonText ctermfg=gray
