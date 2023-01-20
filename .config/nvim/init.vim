syntax on
set shiftwidth=4
set tabstop=4
set softtabstop=4
set autoindent
set mouse=
set number relativenumber
" filetype plugin indent on

call plug#begin()

Plug 'neoclide/coc.nvim' " auto-completion
Plug 'preservim/nerdtree' " Nerdtree
Plug 'vim-airline/vim-airline' " vim-airline
Plug 'tpope/vim-commentary' " Comment lines
Plug 'tpope/vim-surround' " surrounding
Plug 'preservim/tagbar' " tagbar
Plug 'voldikss/vim-floaterm' " terminal
Plug 'arcticicestudio/nord-vim' " nord colorscheme
Plug 'nvim-treesitter/nvim-treesitter', {'do': ':TSUpdate'} " treesitter
Plug 'Vimjas/vim-python-pep8-indent' " python indentation

call plug#end()

" shortcuts
nnoremap <C-f> :NERDTreeFocus<CR>
nnoremap <C-n> :NERDTree<CR>
nnoremap <C-t> :NERDTreeToggle<CR>
nmap <F9> :TagbarToggle<CR>

" save session, write changes and exit
func SaveSession(path)
	NERDTreeClose
	FloatermKill
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
func OpenRanger()
	:FloatermNew --height=0.6 --width=0.4 --wintype=float --name=filemanager
				\ --position=topleft --autoclose=2 ranger --cmd="cd ~"
endfunc
command! Ranger call OpenRanger()

let g:floaterm_keymap_toggle = '<Leader>t'
" let g:floaterm_wintype = 'split'
" let g:floaterm_height = 0.4

let NERDTreeShowHidden = 1

" colorscheme
colorscheme nord

" better syntax highlight
lua <<EOF
require'nvim-treesitter.configs'.setup {
	ensure_installed = {"python", "html"}, -- one of "all", "maintained" (parsers with maintainers), or a list of languages
	ignore_install = {}, -- List of parsers to ignore installing
	highlight = {
		enable = true,              -- false will disable the whole extension
		disable = {},  -- list of language that will be disabled
		-- Setting this to true will run `:h syntax` and tree-sitter at the same time.
		-- Set this to `true` if you depend on 'syntax' being enabled (like for indentation).
	    -- Using this option may slow down your editor, and you may see some duplicate highlights.
		-- Instead of true it can also be a list of languages
		additional_vim_regex_highlighting = false,
  },
}
EOF

" change color when line reaches max chars (81)
highlight OverLength ctermbg=red ctermfg=white guibg=#000000
match OverLength /\%81v.\+/

" python indentation settings
" autocmd FileType python setlocal indentkeys-=:
" autocmd FileType python setlocal indentkeys-=<:>

" baaammm
no <Up> <Nop>
no <Down> <Nop>
no <Left> <Nop>
no <Right> <Nop>
ino <Up> <Nop>
ino <Down> <Nop>
ino <Left> <Nop>
ino <Right> <Nop>
