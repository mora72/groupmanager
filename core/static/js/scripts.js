$( document ).ready(function() {
    // configuração do botão deletar
    var deleteBtn = $('#btndelete');
    $(deleteBtn).on('click', function(e) {
        e.preventDefault();
        var delLink = $(this).attr('href');
        var result = confirm('Confirma remoção ? ');
        if(result) {
            window.location.href = delLink;
        }
    });

    // configuração do filtro uf
    var filteruf     = $('#filteruf');
    var baseUrl   = 'http://localhost:8000/';

    // configuração do filtro grupo
    var filtergrupo     = $('#filtergrupo');

    // configuração do filtro status
    var filterstatus     = $('#filterstatus');
    var baseUrlIntegrantes   = 'http://localhost:8000/integrantes/';

    // configuração da busca grupo
    var searchBtnGrupo = $('#searchgrupo-btn');
    var searchFormGrupo = $('#searchgrupo-form');

    // configuração da busca integrante
    var searchBtnIntegrante = $('#searchintegrante-btn');
    var searchFormIntegrante = $('#searchintegrante-form');

    // configuração da busca cidade de interesse
    var searchBtnCidadeInteresse = $('#search-btn-cidadeinteresse');
    var searchFormCidadeInteresse = $('#searchcidadeinteresse-form');

    // Ação da busca Grupo (click)
    $(searchBtnGrupo).on('click', function() {
        console.log('entrei grupo')
        searchFormGrupo.submit();
    });

    // Ação do filtro uf (change)
    $(filteruf).change(function() {
        var filteruf = $(this).val();
        window.location.href = baseUrl + '?filteruf=' + filteruf;
    });

   // Ação da busca Integrante (click)
    $(searchBtnIntegrante).on('click', function() {
        console.log('entrei integrante')
        searchFormIntegrante.submit();
    });

    // Ação da busca Cidade de Interesse (click)
    $(searchBtnCidadeInteresse).on('click', function() {
        searchFormCidadeInteresse.submit();
    });

    // Ação do filtro status (change)
    $(filterstatus).change(function() {
        var filterstatus = $(this).val();
        var filtergrupo = $('#filtergrupo').val();
        window.location.href = baseUrlIntegrantes + '?filterstatus=' + filterstatus + '&filtergrupo=' + filtergrupo;
    });

    // Ação do filtro grupo (change)
    $(filtergrupo).change(function() {
        var filtergrupo = $(this).val();
        var filterstatus = $('#filterstatus').val();
        window.location.href = baseUrlIntegrantes + '?filtergrupo=' + filtergrupo + '&filterstatus=' + filterstatus;
    });
});
