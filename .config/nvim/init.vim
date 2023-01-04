:set shiftwidth=4
:set tabstop=4
:set softtabstop=4
:set autoindent
:set mouse=a
:set number relativenumber
syntax on

call plug#begin()

Plug 'neoclide/coc.nvim' " auto-completion
Plug 'preservim/nerdtree' " Nerdtree
Plug 'vim-airline/vim-airline' " vim-airline
Plug 'jiangmiao/auto-pairs' " auto-close braces
Plug 'tpope/vim-commentary' " Comment lines
Plug 'tpope/vim-surround' " surrounding
Plug 'preservim/tagbar' " tagbar
Plug 'voldikss/vim-floaterm' " terminal
Plug 'arcticicestudio/nord-vim' " nord colorscheme
Plug 'nvim-treesitter/nvim-treesitter', {'do': ':TSUpdate'} " treesitter

call plug#end()

" shortcuts
nnoremap <C-f> :NERDTreeFocus<CR>
nnoremap <C-n> :NERDTree<CR>
nnoremap <C-t> :NERDTreeToggle<CR>

" save session, write changes and exit
function SaveSession(path)
	NERDTreeClose
	execute "mksession! ~/.config/nvim/sessions/" .. a:path
	xa
endfunction

command! -nargs=1 Xs call SaveSession(<f-args>)

nnoremap <Leader>ss :Xs 
nnoremap <Leader>os :source ~/.config/nvim/sessions/
nnoremap <Leader>rs :!rm ~/.config/nvim/sessions/

nmap <F12> :TagbarToggle<CR>

let g:floaterm_keymap_toggle = '<Leader>t'
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
highlight OverLength ctermbg=red ctermfg=white guibg=#592929
match OverLength /\%81v.\+/
