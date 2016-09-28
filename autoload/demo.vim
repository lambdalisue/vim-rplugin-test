if has('nvim')
  function! demo#regget(regname) abort
    return _demo_regget(a:regname)
  endfunction

  function! demo#regset(regname, value) abort
    call _demo_regset(a:regname, a:value)
  endfunction
else
  function! demo#regget(regname) abort
    return demo#rplugin#regget(a:regname)
  endfunction

  function! demo#regset(regname, value) abort
    call demo#rplugin#regset(a:regname, a:value)
  endfunction
endif
