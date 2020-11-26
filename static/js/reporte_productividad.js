//Modelo 1
var Modelo1 = {
    dibujar: function (response) {
        var orden = response.numeral.orden;
        switch (orden) {
            case 6: $("#modelo1Crear" + `${response.numeral.id}`).before(
                `<form id="modelo1/${response.id}" enctype="multipart/form-data">
                        <div class="pt-4 pr-4 pl-4">                            
                            <div class="form-group row">
                                <label for="autores" class="col-md-2 ">Autor(es):</label>
                                <div class="col-md-10">
                                    <input class="mb-1 form-control" id="autoresModelo1${response.id}" name="autores" type="text">
                                </div>
                            </div>

                            <div class="form-group row">
                                <label for="titulo" class="col-md-2 ">Titulo:</label>
                                <div class="col-md-10">
                                    <input class="mb-1 form-control" id="tituloModelo1${response.id}" name="titulo" type="text">
                                </div>
                            </div>

                            <div class="form-group row">
                                <label for="revista" class="col-md-2 ">Revista o Publicación:</label>
                                <div class="col-md-10">
                                    <input class="mb-1 form-control" id="revista_publicacionModelo1${response.id}" name="revista_publicacion"
                                        type="text">
                                </div>
                            </div>

                            <div class="form-group row">
                                <label for="url" class="col-md-2 ">URL:</label>
                                <div class="col-md-10">
                                    <input class="mb-1 form-control" id="urlModelo1${response.id}" name="url" type="url">
                                </div>
                            </div>


                            <div class="form-group row">
                                <label for="DOI/ISBN" class="col-md-2 ">DOI/ISBN: </label>
                                <div class="col-md-10">
                                    <input class="mb-1 form-control" type="text" name="doi" id="doiModelo1${response.id}">
                                </div>
                            </div>

                            <div class="form-group row">
                                <label for="" class="col-md-2 ">Fecha:</label>
                                <div class="col-md-10">
                                    <input maxlength="7" class="form-control mb-1" type="text" name="fecha" placeholder="Ingrese la fecha en formato YYYY/MM"
                                        id="fechaModelo1${response.id}">
                                </div>
                            </div>

                            <div class="form-group row">
                                <label for="estudiantes" class="col-md-2 ">Estudiante(s):</label>
                                <div class="col-md-10">
                                    <input class="mb-1 form-control" id="estudiantesModelo1${response.id}" name="estudiantes" type="text">
                                </div>
                            </div>

                            <input class="form-control" type="file" accept=".pdf, image/*" name="anexo"
                                id="anexoModelo1${response.id}">
                            <small class="mb-4">Tamaño máximo: 5 Mb</small>

                            <div class="justify-content-end d-flex">
                                <div class="row">
                                    <div class="col-12">
                                        <button type="button" class="btn btn-success actualizar " title="Guardar cambios"><i class="fas fa-save">&nbsp;Guardar</i></button>
                                        <button class="btn btn-warning text-white editar" type="reset"><i class="fas fa-ban text-white"></i>&nbsp;Cancelar</button>
                                        <button type="button" class="btn btn-primary editar" title="Editar entrada"><i class="fas fa-edit">&nbsp;Editar</i></button>
                                        <button type="button" class="btn btn-danger eliminar" title="Eliminar entrada"><i class="fas fa-trash-alt">&nbsp;Eliminar</i></button>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </form>
                    <hr>`);
                break;
            case 8: $("#modelo1Crear" + `${response.numeral.id}`).before(
                `<form id="modelo1/${response.id}" enctype="multipart/form-data">
                        <div class="pt-4 pr-4 pl-4">   
                            <div class="form-group row">
                                <label for="autores" class="col-md-2 ">Autor(es):</label>
                                <div class="col-md-10">
                                    <input class="mb-1 form-control" id="autoresModelo1${response.id}" name="autores" type="text">
                                </div>
                            </div>

                            <div class="form-group row">
                                <label for="titulo" class="col-md-2 ">Titulo:</label>
                                <div class="col-md-10">
                                    <input class="mb-1 form-control" id="tituloModelo1${response.id}" name="titulo" type="text">
                                </div>
                            </div>

                            <div class="form-group row">
                                <label for="revista" class="col-md-2 ">Revista o Publicación:</label>
                                <div class="col-md-10">
                                    <input class="mb-1 form-control" id="revista_publicacionModelo1${response.id}" name="revista_publicacion" type="text">
                                </div>
                            </div>

                            <div class="form-group row">
                                <label for="url" class="col-md-2 ">URL:</label>
                                <div class="col-md-10">
                                    <input class="mb-1 form-control" id="urlModelo1${response.id}" name="url" type="url">
                                </div>
                            </div>

                            <div class="form-group row">
                                <label for="" class="col-md-2 ">Fecha:</label>
                                <div class="col-md-10">
                                    <input maxlength="7" class="form-control mb-1" type="text" name="fecha" id="fechaModelo1${response.id}">
                                </div>
                            </div>

                            <div class="form-group row">
                                <label for="estudiantes" class="col-md-2 ">Estudiante(s):</label>
                                <div class="col-md-10">
                                    <input class="mb-1 form-control" id="estudiantesModelo1${response.id}" name="estudiantes" type="text">
                                </div>
                            </div>

                            <input class="form-control" type="file" accept=".pdf, image/*" name="anexo" id="anexoModelo1${response.id}">
                            <small class="mb-4">Tamaño máximo: 5 Mb</small>

                            <div class="justify-content-end d-flex">
                                <div class="row">
                                    <div class="col-12">
                                        <button type="button" class="btn btn-success actualizar" title="Guardar cambios"><i class="fas fa-save">&nbsp;Guardar</i></button>

                                        <button class="btn btn-warning text-white editar" type="reset">
                                            <i class="fas fa-ban text-white"></i>&nbsp;Cancelar</button>

                                        <button type="button" class="btn btn-primary editar"
                                            title="Editar entrada"><i class="fas fa-edit">&nbsp;Editar</i></button>

                                        <button type="button" class="btn btn-danger eliminar"
                                            title="Eliminar entrada"><i class="fas fa-trash-alt">&nbsp;Eliminar</i></button>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </form>
                    <hr>`);

                break;
            case 9: $("#modelo1Crear" + `${response.numeral.id}`).before(
                    `<form id="modelo1/${response.id}" enctype="multipart/form-data">
                            <div class="pt-4 pr-4 pl-4">
                                
    
                                <div class="form-group row">
                                    <label for="autores" class="col-md-2 ">Autor(es):</label>
                                    <div class="col-md-10">
                                        <input class="mb-1 form-control" id="autores${response.id}" name="autores" type="text">
                                    </div>
                                </div>
    
                                <div class="form-group row">
    
                                    <label for="titulo" class="col-md-2 ">Titulo:</label>
                                    <div class="col-md-10">
                                        <input class="mb-1 form-control" id="titulo${response.id}" name="titulo" type="text">
                                    </div>
    
                                </div>
    
                                <div class="form-group row">
                                    <label for="revista" class="col-md-2 ">Revista o Publicación:</label>
                                    <div class="col-md-10">
                                        <input class="mb-1 form-control" id="revista_publicacion${response.id}" name="revista_publicacion" type="text">
                                    </div>
                                </div>
    
                                <div class="form-group row">
                                    <label for="" class="col-md-2 ">Fecha:</label>
                                    <div class="col-md-10">
                                        <input maxlength="7" class="form-control mb-1" type="text" name="fecha"
                                            id="fecha${response.id}" placeholder="Ingrese la fecha en formato YYYY/MM">
                                    </div>
                                </div>
    
                                <div class="form-group row">
                                    <label for="estudiantes" class="col-md-2">Estudiante(s):</label>
                                    <div class="col-md-10">
                                        <input class="mb-1 form-control" id="estudiantes${response.id}" name="estudiantes"" type="text">
                                    </div>
                                </div>
    
                                <input class="form-control" type="file" accept=".pdf, image/*" name="anexo" id="anexo${response.id}">
                                <small class="mb-4">Tamaño máximo: 5 Mb</small>
    
                                <div class="justify-content-end d-flex">
                                    <div class="row">
                                        <div class="col-12">
                                            <button type="button" class="btn btn-success actualizar" title="Guardar cambios"><i class="fas fa-save">&nbsp;Guardar</i></button>
    
                                            <button class="btn btn-warning text-white editar" type="reset"><i class="fas fa-ban text-white"></i>&nbsp;Cancelar</i></button>
    
                                            <button type="button" class="btn btn-primary editar" title="Editar entrada"><i class="fas fa-edit">&nbsp;Editar</i></button>
    
                                            <button type="button" class="btn btn-danger eliminar" title="Eliminar entrada"><i class="fas fa-trash-alt">&nbsp;Eliminar</i></button>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </form>`);
                    break;         
            case 10: $("#modelo1Crear" + `${response.numeral.id}`).before(
                `<form id="modelo1/${response.id}" enctype="multipart/form-data">
                        <div class="pt-4 pr-4 pl-4">
                            
                            <div class="form-group row">
                                <label for="autores" class="col-md-2 ">Autor(es):</label>
                                <div class="col-md-10">
                                    <input class="mb-1 form-control" id="autoresModelo1${response.id}" name="autores" type="text">
                                </div>
                            </div>

                            <div class="form-group row">
                                <label for="titulo" class="col-md-2 ">Titulo:</label>
                                <div class="col-md-10">
                                    <input class="mb-1 form-control" id="tituloModelo1${response.id}" name="titulo" type="text">
                                </div>
                            </div>

                            <div class="form-group row">
                                <label for="revista" class="col-md-2 ">Revista o Publicación:</label>
                                <div class="col-md-10">
                                    <input class="mb-1 form-control" id="revista_publicacionModelo1${response.id}" name="revista_publicacion" type="text">
                                </div>
                            </div>

                            <div class="form-group row">
                                <label for="" class="col-md-2 ">Fecha:</label>
                                <div class="col-md-10">
                                    <input maxlength="7" class="form-control mb-1" type="text" name="fecha" id="fechaModelo1${response.id}">
                                </div>
                            </div>

                            <div class="form-group row">
                                <label for="estudiantes" class="col-md-2 ">Estudiante(s):</label>
                                <div class="col-md-10">
                                    <input class="mb-1 form-control" id="estudiantesModelo1${response.id}" name="estudiantes" type="text">
                                </div>
                            </div>

                            <input class="form-control" type="file" accept=".pdf, image/*" name="anexo" id="anexoModelo1${response.id}">
                            <small class="mb-4">Tamaño máximo: 5 Mb</small>

                            <div class="justify-content-end d-flex">
                                <div class="row">
                                    <div class="col-12">
                                        <button type="button" class="btn btn-success actualizar " title="Guardar cambios"><i class="fas fa-save">&nbsp;Guardar</i></button>

                                        <button class="btn btn-warning text-white editar" type="reset">
                                            <i class="fas fa-ban text-white"></i>&nbsp;Cancelar</button>

                                        <button type="button" class="btn btn-primary editar" title="Editar entrada"><i
                                                class="fas fa-edit">&nbsp;Editar</i></button>

                                        <button type="button" class="btn btn-danger eliminar" title="Eliminar entrada"><i
                                                class="fas fa-trash-alt">&nbsp;Eliminar</i></button>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </form>
                    <hr>`);
                break;
            case 15:
            case 16:
            case 17: $("#modelo1Crear" + `${response.numeral.id}`).before(
                `<form id="modelo1/${response.id}" enctype="multipart/form-data">
                        <div class="pt-4 pr-4 pl-4">   
                            <div class="form-group row">
                                <label for="autores" class="col-md-2 ">Autor(es):</label>
                                <div class="col-md-10">
                                    <input class="mb-1 form-control" id="autoresModelo1${response.id}" name="autores" type="text">
                                </div>
                            </div>

                            <div class="form-group row">
                                <label for="titulo" class="col-md-2 ">Titulo:</label>
                                <div class="col-md-10">
                                    <input class="mb-1 form-control" id="tituloModelo1${response.id}" name="titulo" type="text">
                                </div>
                            </div>

                            <div class="form-group row">
                                <label for="revista" class="col-md-2 ">Revista o Publicación:</label>
                                <div class="col-md-10">
                                    <input class="mb-1 form-control" id="revista_publicacionModelo1${response.id}" name="revista_publicacion" type="text">
                                </div>
                            </div>

                            <div class="form-group row">
                                <label for="url" class="col-md-2 ">URL:</label>
                                <div class="col-md-10">
                                    <input class="mb-1 form-control" id="urlModelo1${response.id}" name="url" type="url">
                                </div>
                            </div>

                            <div class="form-group row">
                                <label for="DOI/ISBN" class="col-md-2 ">DOI/ISBN: </label>
                                <div class="col-md-10">
                                    <input class="mb-1 form-control" type="text" name="doi" id="doiModelo1${response.id}">
                                </div>
                            </div>

                            <input class="form-control" type="file" accept=".pdf, image/*" name="anexo" id="anexoModelo1${response.id}">
                            <small class="mb-4">Tamaño máximo: 5 Mb</small>

                            <div class="justify-content-end d-flex">
                                <div class="row">
                                    <div class="col-12">
                                        <button type="button" class="btn btn-success actualizar " title="Guardar cambios"><i class="fas fa-save">&nbsp;Guardar</i></button>

                                        <button class="btn btn-warning text-white editar" type="reset">
                                            <i class="fas fa-ban text-white"></i>&nbsp;Cancelar</button>

                                        <button type="button" class="btn btn-primary editar "
                                            title="Editar entrada"><i class="fas fa-edit">&nbsp;Editar</i></button>

                                        <button type="button" class="btn btn-danger eliminar" 
                                            title="Eliminar entrada"><i class="fas fa-trash-alt">&nbsp;Eliminar</i></button>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </form>
                    <hr>`);
                break;
            default: $("#modelo1Crear" + `${response.numeral.id}`).before(
                `<form id="modelo1/${response.id}" enctype="multipart/form-data">
                        <div class="pt-4 pr-4 pl-4">
                            
                            <div class="form-group row">
                                <label for="autores" class="col-md-2 ">Autor(es):</label>
                                <div class="col-md-10">
                                    <input class="mb-1 form-control" id="autores${response.id}" name="autores" type="text">
                                </div>
                            </div>

                            <div class="form-group row">

                                <label for="titulo" class="col-md-2 ">Titulo:</label>
                                <div class="col-md-10">
                                    <input class="mb-1 form-control" id="titulo${response.id}" name="titulo" type="text">
                                </div>

                            </div>

                            <div class="form-group row">
                                <label for="revista" class="col-md-2 ">Revista o Publicación:</label>
                                <div class="col-md-10">
                                    <input class="mb-1 form-control" id="revista_publicacion${response.id}" name="revista_publicacion" type="text">
                                </div>
                            </div>

                            <div class="form-group row">
                                <label for="url" class="col-md-2 ">URL:</label>
                                <div class="col-md-10">
                                    <input class="mb-1 form-control" id="url${response.id}" name="url" type="url">
                                </div>
                            </div>

                            <div class="form-group row">
                                <label for="" class="col-md-2 ">DOI/ISBN:</label>
                                <div class="col-md-10">
                                    <input class="form-control mb-1" type="text" name="doi" id="doi${response.id}">
                                </div>
                            </div>

                            <div class="form-group row">
                                <label for="" class="col-md-2 ">BibCode:</label>
                                <div class="col-md-10">
                                    <input class="form-control mb-1" type="text" name="bibcode" id="bibcode${response.id}">
                                </div>
                            </div>

                            <div class="form-group row">
                                <label for="" class="col-md-2 ">Fecha:</label>
                                <div class="col-md-10">
                                    <input maxlength="7" class="form-control mb-1" type="text" name="fecha"
                                        id="fecha${response.id}" placeholder="Ingrese la fecha en formato YYYY/MM">
                                </div>
                            </div>

                            <div class="form-group row">
                                <label for="estudiantes" class="col-md-2">Estudiante(s):</label>
                                <div class="col-md-10">
                                    <input class="mb-1 form-control" id="estudiantes${response.id}" name="estudiantes"" type="text">
                                </div>
                            </div>

                            <input class="form-control" type="file" accept=".pdf, image/*" name="anexo" id="anexo${response.id}">
                            <small class="mb-4">Tamaño máximo: 5 Mb</small>

                            <div class="justify-content-end d-flex">
                                <div class="row">
                                    <div class="col-12">
                                        <button type="button" class="btn btn-success actualizar" title="Guardar cambios"><i class="fas fa-save">&nbsp;Guardar</i></button>
                                        <button  class="btn btn-warning text-white editar" type="reset"><i class="fas fa-ban text-white"></i>&nbsp;Cancelar</i></button>
                                        <button type="button" class="btn btn-primary editar" title="Editar entrada"><i class="fas fa-edit">&nbsp;Editar</i></button>
                                        <button type="button" class="btn btn-danger eliminar" title="Eliminar entrada"><i class="fas fa-trash-alt">&nbsp;Eliminar</i></button>
                                    </div>
                                </div>
                            </div>

                        </div>
                    </form>`);
        
            }
    },
    infoAnterior: function (numeral) {
        var periodo = $("#periodoActual").val();
        var url = "{% url 'reportes:info-anteriorModelo1' %}";
        
        $.ajax({
            type: "GET",
            url: "http://127.0.0.1:8000/info-anteriorModelo1",
            data: {
                'periodo': periodo,
                'numeral': numeral
            },
            dataType: "json",
        })
            .done(function (response) {
                if (response.autores.length != 0) {
                    $('#sinEntradas' + numeral).remove();
                    for (let i = 0; i < response.autores.length; i++) {
                        data = {}
                        data['numeral'] = response.numeral[0];
                        data['id'] = response.ids[i];
                        Modelo1.dibujar(data)
                        $("#autoresModelo1" + response.ids[i]).val(response.autores[i])
                        $("#tituloModelo1" + response.ids[i]).val(response.titulo[i])
                        $("#revista_publicacionModelo1" + response.ids[i]).val(response.revista_publicacion[i])
                        $("#urlModelo1" + response.ids[i]).val(response.url[i])
                        $("#doiModelo1" + response.ids[i]).val(response.doi[i])
                        $("#fechaModelo1" + response.ids[i]).val(response.fecha[i])
                        $("#bibcodeModelo1" + response.ids[i]).val(response.bibcode[i])
                        $("#paginasModelo1" + response.ids[i]).val(response.paginas[i])
                        $("#volumenModelo1" + response.ids[i]).val(response.volumen[i])
                        $("#estudiantesModelo1" + response.ids[i]).val(response.estudiantes[i])
                    }
                    $("#infoAnteriorModelo1" + numeral).remove();
                    notificacion.importarPeriodo();

                }
                else {
                    notificacion.errorImportarPeriodo();
                }
            });
    }
}
//Fin modelo1

//Modelo 2
var Modelo2 = {
    dibujar: function (response) {
        $("#modelo2Crear" + `${response.numeral.id}`).before(
            `<form id="modelo2/${response.id}" enctype="multipart/form-data">
                    <div class="pt-4 pr-4 pl-4">

                        <div class="form-group">
                            
                            <div class="form-group row">
                                <label for="nombre_del_proyecto" class="col-md-2">Nombre del proyecto:</label>
                                <div class="col-md-10">
                                    <input class="form-control mb-1" type="text" name="nombre_del_proyecto" id="nombre_del_proyectoModelo2${response.id}">
                                </div>
                            </div>

                            <div class="form-group row">
                                <label for="Participantes" class="col-md-2">Participantes:</label>
                                <div class="col-md-10">
                                    <input class="form-control mb-1" type="text" name="participantes" id="participantesModelo2${response.id}">
                                </div>
                            </div>

                            <div class="form-group row">
                                <label for="Estudiantes" class="col-md-2">Estudiantes:</label>
                                <div class="col-md-10">
                                    <input class="form-control mb-1" type="text" name="estudiantes" id="estudiantesModelo2${response.id}">
                                </div>
                            </div>

                            <div class="form-group row">
                                <label for="rol" class="col-md-2">Rol:</label>
                                <div class="col-md-10">
                                    <select class="form-control mb-1" name="rol" required id="responsableModelo2${response.id}">
                                        <option value="" selected disabled>------------------------</option>
                                        <option value="Responsable técnico">Responsable técnico</option>
                                        <option value="Participante">Participante</option>
                                    </select>
                                </div>
                            </div>

                            <label for="Descripcion">Descripcion</label>
                            <textarea class="form-control mb-1" name="descripcion" id="descripcionModelo2${response.id}" cols="30" rows="5"></textarea>

                            <input class="form-control" type="file" accept=".pdf, image/*" name="anexo" id="anexoModelo2${response.id}">
                            <small class="mb-4">Tamaño máximo: 5 Mb</small>

                            <div class="justify-content-end d-flex">
                                <div class="row">
                                    <div class="col-12">
                                        <button type="button" class="btn btn-success actualizar" title="Guardar cambios"><i class="fas fa-save">&nbsp;Guardar</i></button>

                                        <button class="btn btn-warning text-white editar" type="reset"><i class="fas fa-ban text-white">&nbsp;Cancelar</i></button>

                                        <button type="button" class="btn btn-primary editar"  title="Editar entrada"><i class="fas fa-edit">&nbsp;Editar</i></button>
                                        
                                        <button type="button" class="btn btn-danger eliminar" title="Eliminar entrada"><i class="fas fa-trash-alt">&nbsp;Eliminar</i></button>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </form>
                <hr>`);
    },
    infoAnterior: function (numeral) {
        var periodo = $("#periodoActual").val();

        $.ajax({
            type: "GET",
            url: "http://127.0.0.1:8000/info-anteriorModelo2",
            data: {
                'periodo': periodo,
                'numeral': numeral,
            },
            dataType: "json",
        })
            .done(function (response) {
                if (response.descripcion.length != 0) {
                    $('#sinEntradas' + numeral).remove()
                    for (let i = 0; i < response.descripcion.length; i++) {
                        data = {}
                        data['numeral'] = response.numeral[0];
                        data['id'] = response.ids[i];
                        Modelo2.dibujar(data)
                        $("#nombre_del_proyectoModelo2" + response.ids[i]).val(response.nombre_del_proyecto[i]);
                        $("#descripcionModelo2" + response.ids[i]).val(response.descripcion[i]);
                        $("#participantesModelo2" + response.ids[i]).val(response.participantes[i]);
                        $("#responsableModelo2" + response.ids[i]).val(response.rols[i]);
                        $("#estudiantesModelo2" + response.ids[i]).val(response.estudiantes[i]);
                    }
                    $("#infoAnteriorModelo2" + numeral).remove();
                    notificacion.importarPeriodo();

                }
                else {
                    notificacion.errorImportarPeriodo();
                }

            })
            .fail(function (response) {
                notificacion.error(response);
            });
    },
}
//Fin modelo2

//Modelo 3
var Modelo3 = {
    dibujar: function (response) {
        $("#modelo3Crear" + `${response.numeral.id}`).before(
            `<form class="pt-4 pr-4 pl-4" id="modelo3/${response.id}" enctype="multipart/form-data">
                    
                        <div class="form-group row">
                            <label for="conferencia_proyecto" class="col-md-2 ">Conferencia o proyecto:</label>
                            <div class="col-md-10">
                                <input class="mb-1 form-control" id="conferencia_proyectoModelo3${response.id}" name="conferencia_proyecto" type="text">
                            </div>
                        </div>

                        <div class="form-group row">
                            <label for="rol" class="col-md-2 ">Rol:</label>
                            <div class="col-md-10">
                                <input class="mb-1 form-control" id="rolModelo3${response.id}" name="rol" type="text">
                            </div>
                        </div>

                        <div class="form-group row">
                            <label for="url" class="col-md-2 ">URL:</label>
                            <div class="col-md-10">
                                <input class="mb-1 form-control" id="urlModelo3${response.id}" name="url" type="text">
                            </div>
                        </div>

                        <div class="form-group row">
                            <label for="fecha" class="col-md-2 ">Fecha: </label>
                            <div class="col-md-10">
                                <input class="mb-1 form-control" id="fechaModelo3${response.id}" name="fecha" type="text">
                            </div>
                        </div>

                        <input class="form-control" type="file" accept=".pdf, image/*" name="anexo" id="anexoModelo3${response.id}">
                        <small class="mb-4">Tamaño máximo: 5 Mb</small>

                        <div class="justify-content-end d-flex">
                            <div class="row">
                                <div class="col-12">
                                    <button type="button" class="btn btn-success actualizar" title="Guardar cambios">
                                        <i class="fas fa-save">&nbsp;Guardar</i></button>

                                    <button class="btn btn-warning  text-white editar" type="reset">
                                        <i class="fas fa-ban text-white"></i>&nbsp;Cancelar</i></button>

                                    <button type="button" class="btn btn-primary editar"
                                        title="Editar entrada"><i class="fas fa-edit">&nbsp;Editar</i></button>
                                    <button type="button" class="btn btn-danger eliminar"
                                        title="Eliminar entrada"><i class="fas fa-trash-alt">&nbsp;Eliminar</i></button>
                                </div>
                            </div>
                        </div>
                </form>
                <hr>`);
    },
    infoAnterior: function (numeral) {
        var periodo = $("#periodoActual").val();
        $.ajax({
            type: "GET",
            url: "http://127.0.0.1:8000/info-anteriorModelo3",
            data: {
                'periodo': periodo,
                'numeral': numeral,
            },
            dataType: "json",
        })
            .done(function (response) {
                if (response.conferencia_proyecto.length != 0) {
                    $('#sinEntradas' + numeral).remove()
                    for (var i = 0; i < response.conferencia_proyecto.length; i++) {
                        data = {}
                        data['numeral'] = response.numeral[0];
                        data['id'] = response.ids[i];
                        Modelo3.dibujar(data);
                        $("#conferencia_proyectoModelo3" + response.ids[i]).val(response.conferencia_proyecto[i])
                        $("#rolModelo3" + response.ids[i]).val(response.rol[i])
                        $("#urlModelo3" + response.ids[i]).val(response.urls[i])
                        $("#fechaModelo3" + response.ids[i]).val(response.fecha[i])
                    }
                    notificacion.importarPeriodo();
                    $("#infoAnteriorModelo3" + numeral).remove();

                } else {
                    notificacion.errorImportarPeriodo();
                }

            });
    }
}
//Fin modelo3

//Modelo4
var Modelo4 = {
    dibujar: function (response, info_anterior=false) {
        var orden = response.numeral.orden;
        switch (orden) {
            case 26:
            case 27: $("#modelo4Crear" + `${response.numeral.id}`).before(
                `<form id="modelo4/${response.id}" enctype="multipart/form-data">
                        <div class="pt-4 pr-4 pl-4">
                            
                            <div class="form-group row">
                                <label for="" class="col-md-2 ">Título:</label>
                                <div class="col-md-10">
                                    <input class="form-control mb-1" type="text" name="titulo" id="tituloModelo4${response.id}">
                                </div>
                            </div>

                            <div class="form-group row">
                                <label for="" class="col-md-2 ">Nombre conferencia:</label>
                                <div class="col-md-10">
                                    <input class="form-control mb-1" type="text" name="nombre_de_conferencia" id="nombre_de_conferenciaModelo4${response.id}">
                                </div>
                            </div>

                            <div class="form-group row">
                                <label for="" class="col-md-2 ">Fecha:</label>
                                <div class="col-md-10">
                                    <input class="form-control mb-1" type="text" name="fecha" id="fechaModelo4${response.id}">
                                </div>
                            </div>

                            <div class="form-group row">
                                <label for="" class="col-md-2 ">URL:</label>
                                <div class="col-md-10">
                                    <input class="form-control mb-1" type="url" name="url" id="urlModelo4${response.id}">
                                </div>
                            </div>

                            <input class="form-control" type="file" accept=".pdf, image/*" name="anexo" id="anexoModelo4${response.id}">
                            <small class="mb-4">Tamaño máximo: 5 Mb</small>

                            <div class="justify-content-end d-flex">
                                <div class="row">
                                    <div class="col-12">
                                        <button type="button" class="btn btn-success actualizar" title="Guardar cambios"><i class="fas fa-save">&nbsp;Guardar</i></button>

                                        <button class="btn btn-warning text-white editar" type="reset">
                                            <i class="fas fa-ban text-white"></i>&nbsp;Cancelar</i></button>

                                        <button type="button" class="btn btn-primary editar" title="Editar entrada"><i class="fas fa-edit">&nbsp;Editar</i></button>

                                        <button type="button" class="btn btn-danger eliminar"
                                            title="Eliminar entrada"><i class="fas fa-trash-alt">&nbsp;Eliminar</i></button>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </form>
                    <hr>`);
                break;
            default: $("#modelo4Crear" + `${response.numeral.id}`).before(
                `<form id="modelo4/${response.id}" enctype="multipart/form-data">
                        <div class="pt-4 pr-4 pl-4">
                                
                                <div class="form-group row">
                                    <label for="" class="col-md-2 ">Título:</label>
                                    <div class="col-md-10">
                                        <input class="form-control mb-1" type="text" name="titulo"
                                            id="tituloModelo4${response.id}">
                                    </div>
                                </div>

                                <div class="form-group row">
                                    <label for="" class="col-md-2 ">Autores:</label>
                                    <div class="col-md-10">
                                        <input class="form-control mb-1" type="text" name="autores" id="autoresModelo4${response.id}">
                                    </div>
                                </div>

                                <div class="form-group row">
                                    <label for="" class="col-md-2 ">Nombre conferencia:</label>
                                    <div class="col-md-10">
                                        <input class="form-control mb-1" type="text" name="nombre_de_conferencia" id="nombre_de_conferenciaModelo4${response.id}">
                                    </div>
                                </div>

                                <div class="form-group row">
                                    <label for="" class="col-md-2 ">Fecha:</label>
                                    <div class="col-md-10">
                                        <input class="form-control mb-1" type="text" name="fecha" id="fechaModelo4${response.id}">
                                    </div>
                                </div>

                                <div class="form-group row">
                                    <label for="" class="col-md-2 ">Tipo de presentación</label>
                                    <div class="col-md-10">
                                        <select class="form-control mb-1" name="tipo" id="tipoModelo4${response.id}">
                                            <option value="" selected disabled>------------------------</option>
                                            <option value="Presentación Oral">Presentación Oral</option>
                                            <option value="Poster">Poster</option>
                                        </select>
                                    </div>
                                </div>

                                <div class="form-group row">
                                    <label for="" class="col-md-2 ">Estudiantes:</label>
                                    <div class="col-md-10">
                                        <input class="form-control mb-1" type="text" name="estudiantes" id="estudiantesModelo4${response.id}">
                                    </div>
                                </div>

                                <div class="form-group row">
                                    <label for="" class="col-md-2 ">URL:</label>
                                    <div class="col-md-10">
                                        <input class="form-control mb-1" type="url" name="url" id="urlModelo4${response.id}">
                                    </div>
                                </div>

                                <input class="form-control" type="file" accept=".pdf, image/*" name="anexo" id="anexoModelo4${response.id}">
                                <small class="mb-4">Tamaño máximo: 5 Mb</small>

                                <div class="justify-content-end d-flex">
                                    <div class="row">
                                        <div class="col-12">
                                            <button type="button" class="btn btn-success actualizar" title="Guardar cambios"><i class="fas fa-save">&nbsp;Guardar</i></button>

                                            <button class="btn btn-warning text-white editar" type="reset">
                                                <i class="fas fa-ban text-white">&nbsp;Cancelar</i></button>

                                            <button type="button" class="btn btn-primary editar" title="Editar entrada">
                                                <i class="fas fa-edit">&nbsp;Editar</i></button>

                                            <button type="button" class="btn btn-danger eliminar" title="Eliminar entrada">
                                                <i class="fas fa-trash-alt">&nbsp;Eliminar</i></button>
                                        </div>
                                    </div>
                                </div>
                        </div>
                    </form>
                    <hr>`);
                break;
        }
    },
    infoAnterior: function (numeral) {
        var periodo = $("#periodoActual").val();

        $.ajax({
            type: "GET",
            url: "{% url 'reportes:info-anteriorModelo4' %}",
            data: {
                'periodo': periodo,
                'numeral': numeral,
            },
            dataType: "json",
        })
            .done(function (response) {
                if (response.fecha.length != 0) {
                    $('#sinEntradas' + numeral).remove();
                    for (let i = 0; i < response.fecha.length; i++) {

                        data = {}
                        data['numeral'] = response.numeral[0];
                        data['id'] = response.ids[i];

                        Modelo4.dibujar(data)
                        $("#tituloModelo4" + response.ids[i]).val(response.titulo[i]);
                        $("#autoresModelo4" + response.ids[i]).val(response.autores[i]);
                        $("#nombre_de_conferenciaModelo4" + response.ids[i]).val(response.nombre_de_conferencia[i]);
                        $("#fechaModelo4" + response.ids[i]).val(response.fecha[i]);
                        $("#tipoModelo4" + response.ids[i]).val(response.tipo[i]);
                        $("#estudiantesModelo4" + response.ids[i]).val(response.estudiantes[i]);
                        $("#doiModelo4" + response.ids[i]).val(response.doi[i]);
                        $("#urlModelo4" + response.ids[i]).val(response.url[i]);
                    }
                    $("#infoAnteriorModelo4" + numeral).remove();
                    notificacion.importarPeriodo();

                }
                else {
                    notificacion.errorImportarPeriodo();
                }

            })
            .fail(function (response) {
                notificacion.error(response);
            });
    }
}
//FinModelo4

//Modelo 5
var Modelo5 = {
    dibujar: function (response, info_anterior=false) {
        $("#modelo5Crear" + `${response.numeral.id}`).before(
            `<form id="modelo5/${response.id}" enctype="multipart/form-data">
                        <div class="pt-4 pr-4 pl-4">
                            
                            <div class="form-group row">
                                <label for="" class="col-sm-2">Nombre completo:</label>
                                <div class="col-sm-10">
                                    <input class="form-control mb-1" type="text" name="nombre_completo"
                                        id="nombre_completoModelo5${response.id}">
                                </div>
                            </div>
    
                            <div class="form-group row">
                                <label for="" class="col-sm-2">Título de tesis:</label>
                                <div class="col-sm-10">
                                    <input class="form-control mb-1" type="text" name="titulo_de_tesis" id="titulo_de_tesisModelo5${response.id}">
                                </div>
                            </div>
    
                            <div class="form-group row">
                                <label for="" class="col-sm-2">Fecha:</label>
                                <div class="col-sm-10">
                                    <input class="form-control mb-1" type="text" name="fecha" id="fechaModelo5${response.id}">
                                </div>
                            </div>
    
                            <div class="form-group row">
                                <label for="" class="col-sm-2">URL:</label>
                                <div class="col-sm-10">
                                    <input class="form-control mb-1" type="url" name="url" id="urlModelo5${response.id}">
                                </div>
                            </div>
    
                            <input class="form-control" type="file" accept=".pdf, image/*" name="anexo" id="anexoModelo5${response.id}">
                            <small class="mb-4">Tamaño máximo: 5 Mb</small>
    
                            <div class="justify-content-end d-flex">
                                <div class="row">
                                    <div class="col-12">
                                        <button type="button" class="btn btn-success actualizar"
                                            title="Guardar cambios"><i class="fas fa-save">&nbsp;Guardar</i></button>
                                        <button class="btn btn-warning text-white editar"
                                            type="reset">
                                            <i class="fas fa-ban text-white">&nbsp;Cancelar</i></button>
                                        <button type="button" class="btn btn-primary editar"
                                            title="Editar entrada"><i class="fas fa-edit">&nbsp;Editar</i></button>
                                        <button type="button" class="btn btn-danger eliminar"
                                            title="Eliminar entrada"><i class="fas fa-trash-alt">&nbsp;Eliminar</i></button>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <hr>
                    </form>
                `);
    },
    infoAnterior: function (numeral) {
        var periodo = $("#periodoActual").val();
        $.ajax({
            type: "GET",
            url: "{% url 'reportes:info-anteriorModelo5' %}",
            data: {
                'periodo': periodo,
                'numeral': numeral,
            },
            dataType: "json",
        })
            .done(function (response) {
                if (response.nombre_completo.length != 0) {
                    $('#sinEntradas' + numeral).remove()
                    for (let i = 0; i < response.nombre_completo.length; i++) {
                        data = {}
                        data['numeral'] = response.numeral[0];
                        data['id'] = response.ids[i];
                        Modelo5.dibujar(data);
                        $("#nombre_completoModelo5" + response.ids[i]).val(response.nombre_completo[i]);
                        $("#titulo_de_tesisModelo5" + response.ids[i]).val(response.titulo_de_tesis[i]);
                        $("#fechaModelo5" + response.ids[i]).val(response.fecha[i]);
                        $("#urlModelo5" + response.ids[i]).val(response.url[i]);
                    }
                    $("#infoAnteriorModelo5" + numeral).remove();
                    notificacion.importarPeriodo();

                } else {
                    notificacion.errorImportarPeriodo();
                }

            })
            .fail(function (response) {
                notificacion.error(response)
            });
    }
}
//Fin modelo5

//Modelo 6
var Modelo6 = {
    dibujar: function (response) {
        $("#modelo6Crear" + `${response.numeral.id}`).before(
            `<form id="modelo6/${response.id}" enctype="multipart/form-data">
                        <div class="pt-4 pr-4 pl-4">
                            
                            <div class="form-group row">
                                <label for="" class="col-sm-2">Nombre del curso: </label>
                                <div class="col-sm-10">
                                    <input class="form-control mb-1" type="text" name="nombre_del_curso" id="nombre_del_cursoModelo6${response.id}">
                                </div>
                            </div>
    
                            <div class="form-group row">
                                <label for="" class="col-sm-2">Periodo:</label>
                                <div class="col-sm-10">
                                    <input class="form-control mb-1" type="text" name="periodo_numeral" id="periodoModelo6${response.id}">
                                </div>
                            </div>
    
                            <div class="form-group row">
                                <label for="" class="col-sm-2">Notas: </label>
                                <div class="col-sm-10">
                                    <input class="form-control mb-1" type="text" name="notas" id="notasModelo6${response.id}">
                                </div>
                            </div>
    
                            <input class="form-control" type="file" accept=".pdf, image/*" name="anexo" id="anexoModelo6${response.id}">
                            <small class="mb-4">Tamaño máximo: 5 Mb</small>
    
                            <div class="justify-content-end d-flex">
                                <div class="row">
                                    <div class="col-12">
                                        <button type="button" class="btn btn-success actualizar"
                                            title="Guardar cambios"><i class="fas fa-save">&nbsp;Guardar</i></button>
                                        <button class="btn btn-warning text-white editar"
                                            type="reset"><i class="fas fa-ban text-white">&nbsp;Cancelar</i></button>
                                        <button type="button" class="btn btn-primary editar"
                                            id="{{modelo6.id}}" title="Editar entrada"><i class="fas fa-edit">&nbsp;Editar</i></button>
                                        <button type="button" class="btn btn-danger eliminar"
                                            title="Eliminar entrada"><i class="fas fa-trash-alt">&nbsp;Eliminar</i></button>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <hr>
                    </form>`);
    },
    infoAnterior: function (numeral) {
        var periodo = $("#periodoActual").val();
        $.ajax({
            type: "GET",
            url: "http://127.0.0.1:8000/info-anteriorModelo6",
            data: {
                'periodo': periodo,
                'numeral': numeral,
            },
            dataType: "json",
        })
            .done(function (response) {
                if (response.nombre_del_curso.length != 0) {
                    $('#sinEntradas' + numeral).remove()
                    for (let i = 0; i < response.nombre_del_curso.length; i++) {
                        data = {}
                        data['numeral'] = response.numeral[0];
                        data['id'] = response.ids[i];

                        Modelo6.dibujar(data)
                        $("#nombre_del_cursoModelo6" + response.ids[i]).val(response.nombre_del_curso[i]);
                        $("#periodoModelo6" + response.ids[i]).val(response.periodo_numeral[i]);
                        $("#notasModelo6" + response.ids[i]).val(response.notas[i]);
                        $("#infoAnteriorModelo6" + numeral).remove();
                        notificacion.importarPeriodo();

                    }
                }
                else {
                    notificacion.errorImportarPeriodo();
                }

            })
            .fail(function (response) {
                notificacion.error(response)
            });
    }
}
//Fin modelo6

//Modelo 7
var Modelo7 = {
    dibujar: function (response) {
        var orden = response.numeral.orden;
        switch (orden) {
            case 37: $("#modelo7Crear" + `${response.numeral.id}`).before(
                `<form id="modelo7/${response.id}" enctype="multipart/form-data">
                            <div class="pt-4 pr-4 pl-4">
                                
                                <div class="form-group row">
                                    <label for="" class="col-sm-2">Nombre: </label>
                                    <div class="col-sm-10">
                                        <input class="form-control mb-1" type="text" name="nombre" id="nombreModelo7${response.id}">
                                    </div>
                                </div>
    
                                <div class="form-group row">
                                    <label for="" class="col-sm-2">Titulo de tesis: </label>
                                    <div class="col-sm-10">
                                        <input class="form-control mb-1" type="text" name="titulo_de_tesis" id="titulo_de_tesisModelo7${response.id}">
                                    </div>
                                </div>
    
                                <div class="form-group row">
                                    <label for="" class="col-sm-2">Grado: </label>
                                    <div class="col-sm-10">
                                        <select class="form-control mb-1" name="grado" id="gradoModelo7${response.id}">
                                            <option selected disabled value="">-----------------------</option>
                                            <option value="Licenciatura">Licenciatura</option>
                                            <option value="Maestría">Maestría</option>
                                            <option value="Doctorado">Doctorado</option>
                                        </select>
    
                                    </div>
                                </div>
    
                                <div class="form-group row">
                                    <label for="" class="col-sm-2">Institución: </label>
                                    <div class="col-sm-10">
                                        <input class="form-control mb-1" type="text" name="institucion" id="institucionModelo7${response.id}">
                                    </div>
                                </div>
    
                                <div class="form-group row">
                                    <label for="" class="col-sm-2">Notas:</label>
                                    <div class="col-sm-10">
                                        <input class="form-control mb-1" type="text" name="notas" id="notasModelo7${response.id}">
                                    </div>
                                </div>
    
                                <input class="form-control" type="file" accept=".pdf, image/*" name="anexo" id="anexoModelo7${response.id}">
                                <small class="mb-4">Tamaño máximo: 5 Mb</small>
    
                                <div class="justify-content-end d-flex">
                                    <div class="row">
                                        <div class="col-12">
                                            <button type="button" class="btn btn-success actualizar"
                                                title="Guardar cambios"><i class="fas fa-save">&nbsp;Guardar</i></button>
                                            <button class="btn btn-warning text-white editar"
                                                type="reset">
                                                <i class="fas fa-ban text-white"></i>&nbsp;Cancelar</i></button>
                                            <button type="button" class="btn btn-primary editar"
                                                title="Editar entrada"><i class="fas fa-edit">&nbsp;Editar</i></button>
                                            <button type="button" class="btn btn-danger eliminar"
                                                title="Eliminar entrada"><i class="fas fa-trash-alt">&nbsp;Eliminar</i></button>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <hr>
                        </form>`);
                break;

            default: $("#modelo7Crear" + `${response.numeral.id}`).before(
                `<form id="modelo7/${response.id}" enctype="multipart/form-data">
                            <div class="pt-4 pr-4 pl-4">
                                
                                <div class="form-group row">
                                    <label for="" class="col-sm-2">Nombre: </label>
                                    <div class="col-sm-10">
                                        <input class="form-control mb-1" type="text" name="nombre" id="nombreModelo7${response.id}">
                                    </div>
                                </div>
    
                                <div class="form-group row">
                                    <label for="" class="col-sm-2">Titulo de tesis: </label>
                                    <div class="col-sm-10">
                                        <input class="form-control mb-1" type="text" name="titulo_de_tesis" id="titulo_de_tesisModelo7${response.id}">
                                    </div>
                                </div>
    
                                <div class="form-group row">
                                    <label for="" class="col-sm-2">Grado: </label>
                                    <div class="col-sm-10">
                                        <select class="form-control mb-1" name="grado" id="gradoModelo7${response.id}">
                                            <option selected disabled value="">-----------------------</option>
                                            <option value="Maestría">Maestría</option>
                                            <option value="Doctorado">Doctorado</option>
                                        </select>
                                    </div>
                                </div>
    
                                <div class="form-group row">
                                    <label for="" class="col-sm-2">Institución: </label>
                                    <div class="col-sm-10">
                                        <input class="form-control mb-1" type="text" name="institucion" id="institucionModelo7${response.id}">
                                    </div>
                                </div>
    
                                <div class="form-group row">
                                    <label for="" class="col-sm-2">Fecha: </label>
                                    <div class="col-sm-10">
                                        <input class="form-control mb-1" type="text" name="fecha" id="fechaModelo7${response.id}">
                                    </div>
                                </div>
    
                                <div class="form-group row">
                                    <label for="" class="col-sm-2">Notas:</label>
                                    <div class="col-sm-10">
                                        <input class="form-control mb-1" type="text" name="notas" id="notasModelo7${response.id}">
                                    </div>
                                </div>
    
                                <input class="form-control" type="file" accept=".pdf, image/*" name="anexo" id="anexoModelo7${response.id}">
                                <small class="mb-4">Tamaño máximo: 5 Mb</small>
    
                                <div class="justify-content-end d-flex">
                                    <div class="row">
                                        <div class="col-12">
                                            <button type="button" class="btn btn-success actualizar"
                                                title="Guardar cambios"><i class="fas fa-save">&nbsp;
                                                    Guardar</i></button>
                                            <button class="btn btn-warning text-white editar"
                                                type="reset">
                                                <i class="fas fa-ban text-white">&nbsp;Cancelar</i></button>
                                            <button type="button" class="btn btn-primary editar"
                                                title="Editar entrada"><i class="fas fa-edit">&nbsp;Editar</i></button>
                                            <button type="button" class="btn btn-danger eliminar"
                                                title="Eliminar entrada"><i class="fas fa-trash-alt">&nbsp;Eliminar</i></button>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <hr>
                        </form>`);
                break;
        }
    },
    infoAnterior: function (numeral) {
        var periodo = $("#periodoActual").val();
        $.ajax({
            type: "GET",
            url: "http://127.0.0.1:8000/info-anteriorModelo7",
            data: {
                'periodo': periodo,
                'numeral': numeral,
            },
            dataType: "json",
        })
            .done(function (response) {
                if (response.nombre.length != 0) {
                    $('#sinEntradas' + numeral).remove()
                    for (let i = 0; i < response.nombre.length; i++) {

                        data = {}
                        data['numeral'] = response.numeral[0];
                        data['id'] = response.ids[i];

                        Modelo7.dibujar(data)
                        $("#nombreModelo7" + response.ids[i]).val(response.nombre[i]);
                        $("#titulo_de_tesisModelo7" + response.ids[i]).val(response.titulo_de_tesis[i]);
                        $("#gradoModelo7" + response.ids[i]).val(response.grado[i]);
                        $("#institucionModelo7" + response.ids[i]).val(response.institucion[i]);
                        $("#fechaModelo7" + response.ids[i]).val(response.fecha[i]);
                        $("#notasModelo7" + response.ids[i]).val(response.notas[i]);
                    }
                    $("#infoAnteriorModelo7" + numeral).remove()
                    notificacion.importarPeriodo();

                }
                else {
                    notificacion.errorImportarPeriodo();
                }

            })
            .fail(function (response) {
                notificacion.error(response);
            });
    }
}
//Fin modelo7

//Modelo 8
var Modelo8 = {
    dibujar: function (response) {
        $("#modelo8Crear" + `${response.numeral.id}`).before(
            `<form id="modelo8/${response.id}" enctype="multipart/form-data">
                    <div class="pt-4 pr-4 pl-4">
                        
                        <div class="form-group row">
                            <label for="" class="col-sm-2">Autor(es): </label>
                            <div class="col-sm-10">
                                <input class="form-control mb-1" type="text" name="autores" id="autoresModelo8${response.id}">
                            </div>
                        </div>

                        <div class="form-group row">
                            <label for="" class="col-sm-2">URL: </label>
                            <div class="col-sm-10">
                                <input class="form-control mb-1" type="text" name="url" id="urlModelo8${response.id}">
                            </div>
                        </div>

                        <label for="">Descripción</label>
                        <textarea class="form-control mb-1" name="descripcion" id="descripcionModelo8${response.id}" cols="30"
                            rows="5"></textarea>

                        <input class="form-control" type="file" accept=".pdf, image/*" name="anexo" id="anexoModelo8${response.id}">
                        <small class="mb-4">Tamaño máximo: 5 Mb</small>

                        <div class="justify-content-end d-flex">
                            <div class="row">
                                <div class="col-12">
                                    <button type="button" class="btn btn-success actualizar"
                                        title="Guardar cambios"><i class="fas fa-save">&nbsp; Guardar</i></button>
                                    <button class="btn btn-warning text-white editar" type="reset">
                                        <i class="fas fa-ban text-white"></i>&nbsp;Cancelar</i></button>
                                    <button type="button" class="btn btn-primary editar"
                                        title="Editar entrada"><i class="fas fa-edit">&nbsp;Editar</i></button>
                                    <button type="button" class="btn btn-danger eliminar"
                                        title="Eliminar entrada"><i class="fas fa-trash-alt">&nbsp;Eliminar</i></button>
                                </div>
                            </div>
                        </div>
                    </div>
                    <hr>
                </form>`);
    },
    infoAnterior: function (numeral) {
        var periodo = $("#periodoActual").val();
        $.ajax({
            type: "GET",
            url: "http://127.0.0.1:8000/info-anteriorModelo8",
            data: {
                'periodo': periodo,
                'numeral': numeral,
            },
            dataType: "json",
        })
            .done(function (response) {
                if (response.autores.length != 0) {
                    $('#sinEntradas' + numeral).remove()
                    for (var i = 0; i < response.autores.length; i++) {
                        data = {}
                        data['numeral'] = response.numeral[0];
                        data['id'] = response.ids[i];

                        Modelo8.dibujar(data)
                        $("#autoresModelo8" + response.ids[i]).val(response.autores[i]);
                        $("#descripcionModelo8" + response.ids[i]).val(response.descripcion[i]);
                        $("#urlModelo8" + response.ids[i]).val(response.url[i]);
                    }
                    $("#infoAnteriorModelo8" + numeral).remove();
                    notificacion.importarPeriodo();

                }
                else {
                    notificacion.errorImportarPeriodo();
                }

            })
            .fail(function (response) {
                notificacion.error(response);
            });
    }
}
//Fin modelo8

//Modelo 9
var Modelo9 = {
    dibujar: function (response) {
        $("#modelo9Crear" + `${response.numeral.id}`).before(
            `<form id="modelo9/${response.id}" enctype="multipart/form-data">
                    <div class="pt-4 pr-4 pl-4">
   
                        <div class="form-group row">
                            <label for="" class="col-sm-2">Nombre: </label>
                            <div class="col-sm-10">
                                <input class="form-control mb-1" type="text" name="nombre" id="nombreModelo9${response.id}">
                            </div>
                        </div>

                        <div class="form-group row">
                            <label for="" class="col-sm-2">Participante(s): </label>
                            <div class="col-sm-10">
                                <input class="form-control mb-1" type="text" name="participantes"
                                    id="participantesModelo9${response.id}">
                            </div>
                        </div>

                        <div class="form-group row">
                            <label for="" class="col-sm-2">Financiamiento: </label>
                            <div class="col-sm-10">
                                <input class="form-control mb-1" type="text" name="financiamiento"
                                    id="financiamientoModelo9${response.id}">
                            </div>
                        </div>

                        <label for="">Descripción: </label>
                        <textarea class="form-control mb-1" name="descripcion" id="descripcionModelo9${response.id}" cols="30"
                            rows="5"></textarea>


                        <input class="form-control" type="file" accept=".pdf, image/*" name="anexo" id="anexoModelo9${response.id}">
                        <small class="mb-4">Tamaño máximo: 5 Mb</small>

                        <div class="justify-content-end d-flex">
                            <div class="row">
                                <div class="col-12">
                                    <button type="button" class="btn btn-success actualizar"
                                        title="Guardar cambios"><i class="fas fa-save">&nbsp;
                                            Guardar</i></button>
                                    <button class="btn btn-warning text-white editar" type="reset">
                                        <i class="fas fa-ban text-white"></i>&nbsp;Cancelar</i></button>
                                    <button type="button" class="btn btn-primary editar"
                                        id="{{modelo9.id}}" title="Editar entrada"><i class="fas fa-edit">&nbsp;Editar</i></button>
                                    <button type="button" class="btn btn-danger eliminar"
                                        title="Eliminar entrada"><i class="fas fa-trash-alt">&nbsp;Eliminar</i></button>
                                </div>
                            </div>
                        </div>
                    </div>
                </form>
                <hr>`);
    },
    infoAnterior: function (numeral) {
        var periodo = $("#periodoActual").val();
        $.ajax({
            type: "GET",
            url: "http://127.0.0.1:8000/info-anteriorModelo9",
            data: {
                'periodo': periodo,
                'numeral': numeral,
            },
            dataType: "json",
        })
            .done(function (response) {
                if (response.nombre.length != 0) {
                    $('#sinEntradas' + numeral).remove()
                    for (var i = 0; i < response.nombre.length; i++) {
                        data = {}
                        data['numeral'] = response.numeral[0];
                        data['id'] = response.ids[i];

                        Modelo9.dibujar(data)
                        $("#nombreModelo9" + response.ids[i]).val(response.nombre[i]);
                        $("#descripcionModelo9" + response.ids[i]).val(response.descripcion[i]);
                        $("#participantesModelo9" + response.ids[i]).val(response.participantes[i]);
                        $("#financiamientoModelo9" + response.ids[i]).val(response.financiamiento[i]);
                    }
                    $("#infoAnteriorModelo9" + numeral).remove();
                    notificacion.importarPeriodo();

                }
                else {
                    notificacion.errorImportarPeriodo();
                }

            })
            .fail(function (response) {
                notificacion.error(response);
            });
    }
}
//Fin modelo9

//Modelo 10
var Modelo10 = {
    dibujar: function (response, info_anterior=false) {
        var orden = response.numeral.orden;
        switch (orden) {
            case 46: $("#modelo10Crear" + `${response.numeral.id}`).before(
                `<form id="modelo10/${response.id}" enctype="multipart/form-data">
                        <div class="pt-4 pr-4 pl-4">
                            
                            <div class="form-group row">
                                <label for="" class="col-sm-2">Título: </label>
                                <div class="col-sm-10">
                                    <input class="form-control mb-1" type="text" name="titulo" id="tituloModelo10${response.id}">
                                </div>
                            </div>
    
                            <div class="form-group row">
                                <label for="" class="col-sm-2">Autor(es): </label>
                                <div class="col-sm-10">
                                    <input class="form-control mb-1" type="text" name="autores" id="autoresModelo10${response.id}">
                                </div>
                            </div>
    
                            <div class="form-group row">
                                <label for="" class="col-sm-2">No. Reporte/ID: </label>
                                <div class="col-sm-10">
                                    <input class="form-control mb-1" type="text" name="numero_reportes" id="NreporteModelo10${response.id}">
                                </div>
                            </div>
    
                            <div class="form-group row">
                                <label for="" class="col-sm-2">Fecha: </label>
                                <div class="col-sm-10">
                                    <input class="form-control mb-1" type="text" name="fecha" id="fechaModelo10${response.id}">
                                </div>
                            </div>
    
                            <div class="form-group row">
                                <label for="" class="col-sm-2">URL: </label>
                                <div class="col-sm-10">
                                    <input class="form-control mb-1" type="text" name="url" id="urlModelo10${response.id}">
                                </div>
                            </div>
    
                            <input class="form-control" type="file" accept=".pdf, image/*" name="anexo" id="anexoModelo10${response.id}">
                            <small class="mb-4">Tamaño máximo: 5 Mb</small>
    
                            <div class="justify-content-end d-flex">
                                <div class="row">
                                    <div class="col-12">
                                        <button type="button" class="btn btn-success actualizar"
                                            title="Guardar cambios"><i class="fas fa-save">&nbsp;
                                                Guardar</i></button>
                                        <button class="btn btn-warning text-white editar"
                                            type="reset"><i class="fas fa-ban text-white"></i>&nbsp;Cancelar</i></button>
                                        <button type="button" class="btn btn-primary editar" title="Editar entrada"><i class="fas fa-edit">&nbsp;Editar</i></button>
                                        <button type="button" class="btn btn-danger eliminar"
                                            title="Eliminar entrada"><i class="fas fa-trash-alt">&nbsp;Eliminar</i></button>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </form>
                    <hr>`);
                break;
            case 48: $("#modelo10Crear" + `${response.numeral.id}`).before(
                `<form id="modelo10/${response.id}" enctype="multipart/form-data">
                    <div class="pt-4 pr-4 pl-4">
   
                        <div class="form-group row">
                            <label for="" class="col-sm-2">Título: </label>
                            <div class="col-sm-10">
                                <input class="form-control mb-1" type="text" name="titulo" id="tituloModelo10${response.id}">
                            </div>
                        </div>

                        <div class="form-group row">
                            <label for="" class="col-sm-2">Autor(es): </label>
                            <div class="col-sm-10">
                                <input class="form-control mb-1" type="text" name="autores" id="autoresModelo10${response.id}">
                            </div>
                        </div>

                        <div class="form-group row">
                            <label for="" class="col-sm-2">Revista o publicación: </label>
                            <div class="col-sm-10">
                                <input class="form-control mb-1" type="text" name="revista_publicacion"
                                    id="revista_publicacionModelo10${response.id}">
                            </div>
                        </div>

                        <div class="form-group row">
                            <label for="" class="col-sm-2">Fecha: </label>
                            <div class="col-sm-10">
                                <input class="form-control mb-1" type="text" name="fecha" id="fechaModelo10${response.id}">
                            </div>
                        </div>

                        <div class="form-group row">
                            <label for="" class="col-sm-2">DOI/ISBN: </label>
                            <div class="col-sm-10">
                                <input class="form-control mb-1" type="text" name="doi" id="doiModelo10${response.id}">
                            </div>
                        </div>

                        <div class="form-group row">
                            <label for="" class="col-sm-2">URL: </label>
                            <div class="col-sm-10">
                                <input class="form-control mb-1" type="text" name="url" id="urlModelo10${response.id}">
                            </div>
                        </div>

                        <input class="form-control" type="file" accept=".pdf, image/*" name="anexo" id="anexoModelo10${response.id}">
                        <small class="mb-4">Tamaño máximo: 5 Mb</small>

                        <div class="justify-content-end d-flex">
                            <div class="row">
                                <div class="col-12">
                                    <button type="button" class="btn btn-success actualizar"
                                        title="Guardar cambios"><i class="fas fa-save">&nbsp;
                                            Guardar</i></button>
                                    <button class="btn btn-warning text-white editar"
                                        type="reset"><i class="fas fa-ban text-white">&nbsp;Cancelar</i></button>
                                    <button type="button" class="btn btn-primary editar"
                                        title="Editar entrada"><i class="fas fa-edit">&nbsp;Editar</i></button>
                                    <button type="button" class="btn btn-danger eliminar"
                                        title="Eliminar entrada"><i class="fas fa-trash-alt">&nbsp;Eliminar</i></button>
                                </div>
                            </div>
                        </div>
                    </div>
                    <hr>
                </form>`)
                break;
        }

    },
    infoAnterior: function (numeral) {
        var periodo = $("#periodoActual").val();
        $.ajax({
            type: "GET",
            url: "http://127.0.0.1:8000/info-anteriorModelo10",
            data: {
                'periodo': periodo,
                'numeral': numeral,
            },
            dataType: "json",
        })
            .done(function (response) {
                if (response.titulo.length != 0) {
                    $('#sinEntradas' + numeral).remove()
                    for (var i = 0; i < response.titulo.length; i++) {
                        data = {}
                        data['numeral'] = response.numeral[0];
                        data['id'] = response.ids[i];

                        Modelo10.dibujar(data)
                        $("#tituloModelo10" + response.ids[i]).val(response.titulo[i]);
                        $("#autoresModelo10" + response.ids[i]).val(response.autores[i]);
                        $("#NreporteModelo10" + response.ids[i]).val(response.numero_reportes[i]);
                        $("#fechaModelo10" + response.ids[i]).val(response.fecha[i]);
                        $("#urlModelo10" + response.ids[i]).val(response.url[i]);
                        $("#doiModelo10" + response.ids[i]).val(response.doi[i]);
                        $("#revista_publicacionModelo10" + response.ids[i]).val(response.revista_publicacion[i]);
                    }

                    $("#infoAnteriorModelo10" + numeral).remove()
                    notificacion.importarPeriodo();
                }
                else {
                    notificacion.errorImportarPeriodo();
                }

            })
            .fail(function (response) {
                notificacion.error(response);
            });
    }
}
//Fin modelo10

//Modelo 11
var Modelo11 = {
    dibujar: function (response, info_anterior=false) {
        $("#modelo11Crear" + `${response.numeral.id}`).before(
            `<form id="modelo11/${response.id}" enctype="multipart/form-data">
                        <div class="pt-4 pr-4 pl-4">
 
                            <div class="form-group row">
                                <label for="" class="col-sm-2">Fecha: </label>
                                <div class="col-sm-10">
                                    <input class="form-control mb-1" type="text" name="fecha" id="fechaModelo11${response.id}">
                                </div>
                            </div>

                            <div class="form-group row">
                                <label for="" class="col-sm-2">URL: </label>
                                <div class="col-sm-10">
                                    <input class="form-control mb-1" type="url" name="url" id="urlModelo11${response.id}">
                                </div>
                            </div>

                            <label for="">Descripción: </label>
                            <textarea class="form-control mb-1" name="descripcion" id="descripcionModelo11${response.id}" cols="30"
                                rows="5"></textarea>

                            <input class="form-control" type="file" accept=".pdf, image/*" name="anexo" id="anexoModelo11${response.id}">
                            <small class="mb-4">Tamaño máximo: 5 Mb</small>

                            <div class="justify-content-end d-flex">
                                <div class="row">
                                    <div class="col-12">
                                        <button type="button" class="btn btn-success actualizar"
                                            title="Guardar cambios"><i class="fas fa-save">&nbsp;Guardar</i></button>
                                        <button  class="btn btn-warning text-white editar" type="reset">
                                            <i class="fas fa-ban text-white">&nbsp;Cancelar</i></button>
                                        <button type="button" class="btn btn-primary editar"
                                            title="Editar entrada"><i class="fas fa-edit">&nbsp;Editar</i></button>
                                        <button type="button" class="btn btn-danger eliminar"
                                            title="Eliminar entrada"><i class="fas fa-trash-alt">&nbsp;Eliminar</i></button>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <hr>
                    </form>`)
    },
    infoAnterior: function (numeral) {
        var periodo = $("#periodoActual").val();
        $.ajax({
            type: "GET",
            url: "http://127.0.0.1:8000/info-anteriorModelo11",
            data: {
                'periodo': periodo,
                'numeral': numeral,
            },
            dataType: "json",
        })
            .done(function (response) {
                if (response.descripcion.length != 0) {
                    $('#sinEntradas' + numeral).remove()
                    for (var i = 0; i < response.descripcion.length; i++) {
                        data = {}
                        data['numeral'] = response.numeral[0];
                        data['id'] = response.ids[i];

                        Modelo11.dibujar(data)
                        $("#fechaModelo11" + response.ids[i]).val(response.fecha[i]);
                        $("#descripcionModelo11" + response.ids[i]).val(response.descripcion[i])
                        $("#urlModelo11" + response.ids[i]).val(response.url[i]);
                    }

                    $("#infoAnteriorModelo11" + numeral).remove()
                    notificacion.importarPeriodo();
                }
                else {
                    notificacion.errorImportarPeriodo();
                }
            });
    }
}
//Fin modelo11

//Modelo 12
var Modelo12 = {
    dibujar: function (response, info_anterior=false) {
        $("#modelo12Crear" + `${response.numeral.id}`).before(
            `<form id="modelo12/${response.id}" enctype="multipart/form-data">
                        <div class="pt-4 pr-4 pl-4">
                            
                            <div class="form-group row">
                                <label class="col-sm-1" for="">Periodo:</label>
                                <div class="col-sm-11">
                                    <input class="form-control mb-1" type="text" name="periodo_numeral" id="periodoModelo12${response.id}">
                                </div>
                            </div>

                            <label for="">Descripcion: </label>
                            <textarea class="form-control mb-1" name="descripcion" id="descripcionModelo12${response.id}" cols="30"
                                rows="5"></textarea>

                            <input class="form-control" type="file" accept=".pdf, image/*" name="anexo" id="anexoModelo12${response.id}">
                            <small class="mb-4">Tamaño máximo: 5 Mb</small>

                            <div class="justify-content-end d-flex">
                                <div class="row">
                                    <div class="col-12">
                                        <button  type="button" class="btn btn-success actualizar"
                                            title="Guardar cambios"><i class="fas fa-save">&nbsp;
                                                Guardar</i></button>
                                        <button  class="btn btn-warning text-white editar"
                                            type="reset">
                                            <i class="fas fa-ban text-white">&nbsp;Cancelar</i></button>
                                        <button type="button" class="btn btn-primary editar" 
                                            title="Editar entrada"><i class="fas fa-edit">&nbsp;Editar</i></button>
                                        <button type="button" class="btn btn-danger eliminar" 
                                            title="Eliminar entrada"><i class="fas fa-trash-alt">&nbsp;Eliminar</i></button>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <hr>
                    </form>`);
    },
    infoAnterior: function (numeral) {
        var periodo = $("#periodoActual").val();
        $.ajax({
            type: "GET",
            url: "http://127.0.0.1:8000/info-anteriorModelo12",
            data: {
                'periodo': periodo,
                'numeral': numeral,
            },
            dataType: "json",
        })
            .done(function (response) {
                if (response.descripcion.length != 0) {
                    $('#sinEntradas' + numeral).remove()
                    for (var i = 0; i < response.descripcion.length; i++) {
                        data = {}
                        data['numeral'] = response.numeral[0];
                        data['id'] = response.ids[i];

                        Modelo12.dibujar(data)
                        $("#periodoModelo12" + response.ids[i]).val(response.periodo_numeral[i]);
                        $("#descripcionModelo12" + response.ids[i]).val(response.descripcion[i]);
                    }

                    $("#infoAnteriorModelo12" + numeral).remove()
                    notificacion.importarPeriodo();
                }
                else {
                    notificacion.errorImportarPeriodo();
                }

            });
    }
}
//Fin modelo12

//Modelo 13
var Modelo13 = {
    dibujar: function (response, info_anterior=false) {
        var orden = parseInt(response.numeral.orden);
        switch (orden) {
            case 38: $("#modelo13Crear" + `${response.numeral.id}`).before(
                `<form id="modelo13/${response.id}" enctype="multipart/form-data">
                            <div class="pt-4 pr-4 pl-4">
                            
                                <div class="form-group row">
                                    <label class="col-sm-2" for="">Nombre estudiante:</label>
                                    <input type="text" class="form-control mb-1 col-sm-10" name="nombre_del_estudiante"
                                        id="nombre_del_estudianteModelo13${response.id}"></input>
                                </div>
        
                                <div class="form-group row">
                                    <label class="col-sm-2" for="">Coordinación:</label>
                                    <input type="text" class="form-control mb-1 col-sm-10" name="coordinacion"
                                        id="coordinacionModelo13${response.id}"></input>
                                </div>
        
                                <div class="form-group row">
                                    <label class="col-sm-2" for="">Grado:</label>
                                    <select class="form-control col-sm-10" name="grado" id="gradoModelo13${response.id}">
                                        <option selected disabled value="">-----------------------</option>
                                        <option value="Maestría">Maestría</option>
                                        <option value="Doctorado">Doctorado</option>
                                    </select>
                                </div>
        
                                <input class="form-control" type="file" accept=".pdf, image/*" name="anexo" id="anexoModelo13${response.id}">
                                <small class="mb-4">Tamaño máximo: 5 Mb</small>
        
                                <div class="justify-content-end d-flex">
                                    <div class="row">
                                        <div class="col-12">
                                            <button type="button" class="btn btn-success actualizar  mr-2"
                                                title="Guardar cambios"><i class="fas fa-save">&nbsp;
                                                    Guardar</i></button>
                                            <button class="btn btn-warning mr-2 text-white"
                                                type="reset">
                                                <i class="fas fa-ban text-white">&nbsp;Cancelar</i></button>
                                            <button type="button" class="btn btn-primary editar mr-2"
                                                title="Editar entrada"><i class="fas fa-edit">&nbsp;Editar</i></button>
                                            <button type="button" class="btn btn-danger eliminar"
                                                title="Eliminar entrada"><i class="fas fa-trash-alt">&nbsp;Eliminar</i></button>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <hr>
                        </form>`);
                break;
            case 53: $("#modelo13Crear" + `${response.numeral.id}`).before(
                `<form id="modelo13/${response.id}" enctype="multipart/form-data">
                    <div class="pt-4 pr-4 pl-4">
                        
                        <div class="form-group row">
                            <label for="" class="col-sm-2">Nombre del estudiante: </label>
                            <div class="col-sm-10">
                                <input class="form-control mb-1" type="text" name="nombre_del_estudiante"
                                    id="nombre_del_estudianteModelo13${response.id}">
                            </div>
                        </div>

                        <label for="">Descripción: </label>
                        <textarea class="form-control mb-1" name="descripcion" id="descripcionModelo13${response.id}" cols="30"
                            rows="5"></textarea>

                        <input class="form-control" type="file" accept=".pdf, image/*" name="anexo" id="anexoModelo13${response.id}">
                        <small class="mb-4">Tamaño máximo: 5 Mb</small>

                        <div class="justify-content-end d-flex">
                            <div class="row">
                                <div class="col-12">
                                    <button  type="button" class="btn btn-success actualizar"
                                        title="Guardar cambios"><i class="fas fa-save">&nbsp;Guardar</i></button>
                                    <button  class="btn btn-warning text-white editar"
                                        type="reset">
                                        <i class="fas fa-ban text-white"></i>&nbsp;Cancelar</i></button>
                                    <button type="button" class="btn btn-primary editar" title="Editar entrada"><i class="fas fa-edit">&nbsp;Editar</i></button>
                                    <button type="button" class="btn btn-danger eliminar" 
                                        title="Eliminar entrada"><i class="fas fa-trash-alt">&nbsp;Eliminar</i></button>
                                </div>
                            </div>
                        </div>
                    </div>
                    <hr>
                </form>`);
                break;
            case 54: $("#modelo13Crear" + `${response.numeral.id}`).before(
                `<form id="modelo13/${response.id}" enctype="multipart/form-data">
                    <div class="pt-4 pr-4 pl-4">
                        
                        <div class="form-group row">
                            <label for="" class="col-sm-2">Nombre del estudiante: </label>
                            <div class="col-sm-10">
                                <input class="form-control mb-1" type="text" name="nombre_del_estudiante"
                                    id="nombre_del_estudianteModelo13${response.id}">
                            </div>
                        </div>

                        <div class="form-group row">
                            <label for="" class="col-sm-2">Fecha: </label>
                            <div class="col-sm-10">
                                <input class="form-control mb-1" type="text" name="fecha" id="fechaModelo13${response.id}">
                            </div>
                        </div>

                        <label for="">Descripción: </label>
                        <textarea class="form-control mb-1" name="descripcion" id="descripcionModelo13${response.id}" cols="30"
                            rows="5"></textarea>

                        <input class="form-control" type="file" accept=".pdf, image/*" name="anexo" id="anexoModelo13${response.id}">
                        <small class="mb-4">Tamaño máximo: 5 Mb</small>

                        <div class="justify-content-end d-flex">
                            <div class="row">
                                <div class="col-12">
                                    <button  type="button" class="btn btn-success actualizar"
                                        title="Guardar cambios"><i class="fas fa-save">&nbsp;
                                            Guardar</i></button>
                                    <button  class="btn btn-warning text-white editar"
                                        type="reset">
                                        <i class="fas fa-ban text-white">&nbsp;Cancelar</i></button>
                                    <button type="button" class="btn btn-primary editar"  title="Editar entrada"><i class="fas fa-edit">&nbsp;Editar</i></button>
                                    <button type="button" class="btn btn-danger eliminar" 
                                        title="Eliminar entrada"><i class="fas fa-trash-alt">&nbsp;Eliminar</i></button>
                                </div>
                            </div>
                        </div>
                    </div>
                    <hr>
                </form>`);
                break;
            default: $("#modelo13Crear" + `${response.numeral.id}`).before(
                `<form id="modelo13/${response.id}" enctype="multipart/form-data">
                    <div class="pt-4 pr-4 pl-4">
                        
                        <div class="form-group row">
                            <label for="" class="col-sm-2">Fecha o periodo: </label>
                            <div class="col-sm-10">
                                <input class="form-control mb-1" type="text" name="fecha" id="fechaModelo13${response.id}">
                            </div>
                        </div>

                        <label for="">Descripción: </label>
                        <textarea class="form-control mb-1" name="descripcion" id="descripcionModelo13${response.id}" cols="30"
                            rows="5"></textarea>

                        <input class="form-control" type="file" accept=".pdf, image/*" name="anexo" id="anexoModelo13${response.id}">
                        <small class="mb-4">Tamaño máximo: 5 Mb</small>

                        <div class="justify-content-end d-flex">
                            <div class="row">
                                <div class="col-12">
                                    <button  type="button" class="btn btn-success actualizar"
                                        title="Guardar cambios"><i class="fas fa-save">&nbsp;
                                            Guardar</i></button>
                                    <button  class="btn btn-warning text-white editar" type="reset">
                                        <i class="fas fa-ban text-white">&nbsp;Cancelar</i></button>
                                    <button type="button" class="btn btn-primary editar" 
                                        title="Editar entrada"><i class="fas fa-edit">&nbsp;Editar</i></button>
                                    <button type="button" class="btn btn-danger eliminar" 
                                        title="Eliminar entrada"><i class="fas fa-trash-alt">&nbsp;Eliminar</i></button>
                                </div>
                            </div>
                        </div>
                    </div>
                    <hr>
                </form>`);
                break;
        }
    },
    infoAnterior: function (numeral) {
        var periodo = $("#periodoActual").val();
        $.ajax({
            type: "GET",
            url: "http://127.0.0.1:8000/info-anteriorModelo13",
            data: {
                'periodo': periodo,
                'numeral': numeral,
            },
            dataType: "json",
        })
            .done(function (response) {
                if (response.nombre_del_estudiante.length != 0) {
                    $('#sinEntradas' + numeral).remove()
                    for (let i = 0; i < response.nombre_del_estudiante.length; i++) {
                        data = {}
                        data['numeral'] = response.numeral[0];
                        data['id'] = response.ids[i];

                        Modelo13.dibujar(data)
                        $("#nombre_del_estudianteModelo13" + response.ids[i]).val(response.nombre_del_estudiante[i]);
                        $("#coordinacionModelo13" + response.ids[i]).val(response.coordinacion[i]);
                        $("#gradoModelo13" + response.ids[i]).val(response.grado[i]);
                        
                        $("#descripcionModelo13" + response.ids[i]).val(response.descripcion[i]);
                        $("#fechaModelo13" + response.ids[i]).val(response.fecha[i]);
                    }
                    $("#infoAnteriorModelo13" + numeral).remove()
                    notificacion.importarPeriodo();

                }
                else {
                    notificacion.errorImportarPeriodo();
                }

            })
            .fail(function (response) {
                notificacion.error(response);
            });
    }
}
//fin Modelo13

//Modelo 14
var Modelo14 = {
    dibujar: function (response, info_anterior=false) {
        $("#modelo14Crear" + `${response.numeral.id}`).before(
            `<form id="modelo14/${response.id}" enctype="multipart/form-data">
                    <div class="pt-4 pr-4 pl-4">
                        
                        <div class="form-group row">
                            <label for="" class="col-sm-2">Fecha o periodo: </label>
                            <div class="col-sm-10">
                                <input class="form-control mb-1" type="text" name="fecha_periodo" id="fecha_periodoModelo14${response.id}">
                            </div>
                        </div>

                        <label for="">Descripción: </label>
                        <textarea class="form-control mb-1" name="descripcion" id="descripcionModelo14${response.id}" cols="30"
                            rows="5"></textarea>

                        <input class="form-control" type="file" accept=".pdf, image/*" name="anexo" id="anexoModelo14${response.id}">
                        <small class="mb-4">Tamaño máximo: 5 Mb</small>

                        <div class="justify-content-end d-flex">
                            <div class="row">
                                <div class="col-12">
                                    <button  type="button" class="btn btn-success actualizar"
                                        title="Guardar cambios"><i class="fas fa-save">&nbsp;
                                            Guardar</i></button>
                                    <button  class="btn btn-warning text-white editar"
                                        type="reset">
                                        <i class="fas fa-ban text-white">&nbsp;Cancelar</i></button>
                                    <button type="button" class="btn btn-primary editar" 
                                        title="Editar entrada"><i class="fas fa-edit">&nbsp;Editar</i></button>
                                    <button type="button" class="btn btn-danger eliminar" 
                                        title="Eliminar entrada"><i class="fas fa-trash-alt">&nbsp;Eliminar</i></button>
                                </div>
                            </div>
                        </div>
                    </div>
                    <hr>
                </form>`);
    },
    infoAnterior: function (numeral) {
        var periodo = $("#periodoActual").val();
        $.ajax({
            type: "GET",
            url: "http://127.0.0.1:8000/info-anteriorModelo14",
            data: {
                'periodo': periodo,
                'numeral': numeral,
            },
            dataType: "json",
        })
            .done(function (response) {
                if (response.descripcion.length != 0) {
                    $('#sinEntradas' + numeral).remove()
                    for (var i = 0; i < response.descripcion.length; i++) {
                        data = {}
                        data['numeral'] = response.numeral[0];
                        data['id'] = response.ids[i];

                        Modelo14.dibujar(data)
                        $("#fecha_periodoModelo14" + response.ids[i]).val(response.fecha_periodo[i]);
                        $("#descripcionModelo14" + response.ids[i]).val(response.descripcion[i]);
                    }

                    $("#infoAnteriorModelo14" + numeral).remove();
                    notificacion.importarPeriodo();
                }
                else { notificacion.errorImportarPeriodo(); }
            })
            .fail(function (response) {
                notificacion.error(response);
            });
    }
}
//Fin modelo14

//Modelo 15
var Modelo15 = {
    dibujar: function (response, info_anterior=false) {
        $("#modelo15Crear" + `${response.numeral.id}`).before(
            `<form id="modelo15/${response.id}" enctype="multipart/form-data">
                <div class="pt-4 pr-4 pl-4">
                    
                    <div class="form-group row">
                        <label class="col-sm-2" for="">Laboratorio o taller: </label>
                        <div class="col-sm-10">
                            <input class="form-control mb-1" type="text" name="laboratorio_taller"
                                id="laboratorio_tallerModelo15${response.id}">
                        </div>
                    </div>

                    <input class="form-control" type="file" accept=".pdf, image/*" name="anexo" id="anexoModelo15${response.id}">
                    <small class="mb-4">Tamaño máximo: 5 Mb</small>

                    <div class="justify-content-end d-flex">
                        <div class="row">
                            <div class="col-12">
                                <button  type="button" class="btn btn-success actualizar"
                                    title="Guardar cambios"><i class="fas fa-save">&nbsp;Guardar</i></button>
                                <button  class="btn btn-warning text-white editar" type="reset">
                                    <i class="fas fa-ban text-white">&nbsp;Cancelar</i></button>
                                <button type="button" class="btn btn-primary editar" 
                                        title="Editar entrada"><i class="fas fa-edit">&nbsp;Editar</i></button>
                                <button type="button" class="btn btn-danger eliminar" 
                                    title="Eliminar entrada"><i class="fas fa-trash-alt">&nbsp;Eliminar</i></button>
                            </div>
                        </div>
                    </div>
                </div>
                <hr>
            </form>`);
    },
    infoAnterior: function (numeral) {
        var periodo = $("#periodoActual").val();
        $.ajax({
            type: "GET",
            url: "http://127.0.0.1:8000/info-anteriorModelo15",
            data: {
                'periodo': periodo,
                'numeral': numeral,
            },
            dataType: "json",
        })
            .done(function (response) {
                if (response.laboratorio_taller.length != 0) {
                    $('#sinEntradas' + numeral).remove()
                    for (var i = 0; i < response.laboratorio_taller.length; i++) {
                        data = {}
                        data['numeral'] = response.numeral[0];
                        data['id'] = response.ids[i];

                        Modelo15.dibujar(data)
                        $("#laboratorio_tallerModelo15" + response.ids[i]).val(response.laboratorio_taller[i]);
                    }
                    $("#infoAnteriorModelo15" + numeral).remove()
                    notificacion.importarPeriodo();

                }
                else {
                    notificacion.errorImportarPeriodo();
                }

            })
            .fail(function (response) {
                notificacion.error(response);
            });
    }
}
//Fin modelo15

//Modelo 16
var Modelo16 = {
    dibujar: function (response, info_anterior=false) {
        $("#modelo16Crear" + `${response.numeral.id}`).before(
            `<form id="modelo16/${response.id}" enctype="multipart/form-data">
                <div class="pt-4 pr-4 pl-4">
                    
                    <div class="form-group row">
                        <label for="" class="col-sm-2">Agencia(s) financiadora(s):</label>
                        <div class="col-sm-10">
                            <input class="form-control mb-1" type="text" name="agencias_financieras"
                                id="agenciaFinanciadoraModelo16${response.id}">
                        </div>
                    </div>

                    <label for="">Descripción: </label>
                    <textarea class="form-control mb-1" name="descripcion" id="descripcionModelo16${response.id}" cols="30"
                        rows="5"></textarea>

                    <input class="form-control" type="file" accept=".pdf, image/*" name="anexo" id="anexoModelo16${response.id}">
                    <small class="mb-4">Tamaño máximo: 5 Mb</small>

                    <div class="justify-content-end d-flex">
                        <div class="row">
                            <div class="col-12">
                                <button  type="button" class="btn btn-success actualizar"
                                    title="Guardar cambios"><i class="fas fa-save">&nbsp;Guardar</i></button>
                                <button  class="btn btn-warning text-white editar"
                                    type="reset">
                                    <i class="fas fa-ban text-white">&nbsp;Cancelar</i></button>
                                <button type="button" class="btn btn-primary editar" 
                                    title="Editar entrada"><i class="fas fa-edit">&nbsp;Editar</i></button>
                                <button type="button" class="btn btn-danger eliminar" 
                                    title="Eliminar entrada"><i class="fas fa-trash-alt">&nbsp;Eliminar</i></button>
                            </div>
                        </div>
                    </div>
                </div>
                <hr>
            </form>`);
    },
    infoAnterior: function (numeral) {
        var periodo = $("#periodoActual").val();
        $.ajax({
            type: "GET",
            url: "http://127.0.0.1:8000/info-anteriorModelo16",
            data: {
                'periodo': periodo,
                'numeral': numeral,
            },
            dataType: "json",
        })
            .done(function (response) {
                if (response.descripcion.length != 0) {
                    $('#sinEntradas' + numeral).remove()
                    for (var i = 0; i < response.descripcion.length; i++) {
                        data = {}
                        data['numeral'] = response.numeral[0];
                        data['id'] = response.ids[i];

                        Modelo16.dibujar(data)
                        $("#descripcionModelo16" + response.ids[i]).val(response.descripcion[i]);
                        $("#agenciaFinanciadoraModelo16" + response.ids[i]).val(response.agencias[i]);
                    }
                    $("#infoAnteriorModelo16" + numeral).remove()
                    notificacion.importarPeriodo();

                }
                else {
                    notificacion.errorImportarPeriodo();
                }

            })
            .fail(function (response) {
                notificacion.error(response);
            });
    }
}
//Fin modelo16

//Modelo 17 
var Modelo17 = {
    dibujar: function (response) {
        $("#modelo17Crear" + `${response.numeral.id}`).before(
            `<form id="modelo17/${response.id}" type="post" enctype="multipart/form-data">
                <div class="pt-4 pr-4 pl-4">
                    <div class="form-group row">
                        <label for="telescopio" class="col-sm-2 col-form-label">Telescopio, instrumento,
                            infraestructura:</label>
                        <div class="col-sm-10">
                            <input class="form-control mb-1" type="text" name="telescopio_instrumento_infra" id="telescopioModelo17${response.id}">
                        </div>
                    </div>

                    <div class="form-group row">
                        <label for="" class="col-sm-2 col-form-label">URL: </label>
                        <div class="col-sm-10">
                            <input class="form-control mb-1" type="text" name="url" id="urlModelo17${response.id}">
                        </div>
                    </div>

                    <label for="">Descripción: </label>
                    <textarea class="form-control mb-1" name="descripcion" id="descripcionModelo17${response.id}" cols="30" rows="5"></textarea>

                    <input class="form-control" type="file" name="anexo" id="anexoModelo17${response.id}">
                    <small class="mb-4">Tamaño máximo: 5 Mb</small>

                    <div class="justify-content-end d-flex">
                        <div class="row">
                            <div class="col-12">
                                <button type="button" class="btn btn-success actualizar" title="Guardar cambios">
                                    <i class="fas fa-save">&nbsp;Guardar</i>
                                </button>

                                <button class="btn btn-warning text-white editar" type="reset">
                                    <i class="fas fa-ban text-white">&nbsp;Cancelar</i>
                                </button>

                                <button type="button" class="btn btn-primary editar" title="Editar entrada">
                                    <i class="fas fa-edit">&nbsp;Editar</i>
                                </button>

                                <button type="button" class="btn btn-danger eliminar" title="Eliminar entrada">
                                    <i class="fas fa-trash-alt">&nbsp;Eliminar</i>
                                </button>
                            </div>
                        </div>
                    </div>
                </div>
            </form>
            <hr>`);
    },
    infoAnterior: function (numeral) {
        var periodo = $("#periodoActual").val();

        $.ajax({
            type: "GET",
            url: "http://127.0.0.1:8000/info-anteriorModelo17",
            data: {
                'periodo': periodo,
                'numeral': numeral,
            },
            dataType: "json",
        })
            .done(function (response) {
                if (response.descripcion.length != 0) {
                    $('#sinEntradas' + numeral).remove()
                    for (var i = 0; i < response.descripcion.length; i++) {
                        data = {}
                        data['numeral'] = response.numeral[0];
                        data['id'] = response.ids[i];
                        Modelo17.dibujar(data);
                        $("#telescopioModelo17" + response.ids[i]).val(response.telescopio[i]);
                        $("#urlModelo17" + response.ids[i]).val(response.urls[i]);
                        $("#descripcionModelo17" + response.ids[i]).val(response.descripcion[i]);
                    }
                    notificacion.importarPeriodo();
                    $("#infoAnteriorModelo17" + numeral).remove();

                } else {
                    notificacion.errorImportarPeriodo();
                }

            });
    }
}
//Fin modelo17

//Modelo 18
var Modelo18 = {
    dibujar: function (response, info_anterior=false) {
        $("#modelo18Crear" + `${response.numeral.id}`).before(
            `<form id="modelo18/${response.id}" enctype="multipart/form-data">
                <div class="pt-4 pr-4 pl-4">
                    
                    <label for="">Descripcion:</label>
                    <textarea class="form-control mb-1" name="descripcion" id="descripcionModelo18${response.id}" cols="30"
                        rows="5"></textarea>

                    <input class="form-control" type="file" accept=".pdf, image/*" name="anexo" id="anexoModelo18${response.id}">
                    <small class="mb-4">Tamaño máximo: 5 Mb</small>

                    <div class="justify-content-end d-flex">
                        <div class="row">
                            <div class="col-12">
                                <button  type="button" class="btn btn-success actualizar"
                                    title="Guardar cambios"><i class="fas fa-save">&nbsp;Guardar</i></button>
                                <button  class="btn btn-warning text-white editar"
                                    type="reset">
                                    <i class="fas fa-ban text-white">&nbsp;Cancelar</i></button>
                                <button type="button" class="btn btn-primary editar" 
                                    title="Editar entrada"><i class="fas fa-edit">&nbsp;Editar</i></button>
                                <button type="button" class="btn btn-danger eliminar" 
                                    title="Eliminar entrada"><i class="fas fa-trash-alt">&nbsp;Eliminar</i></button>
                            </div>
                        </div>
                    </div>
                </div>
                <hr>
            </form>`);
    },
    infoAnterior: function (numeral) {
        var periodo = $("#periodoActual").val();
        $.ajax({
            type: "GET",
            url: "http://127.0.0.1:8000/info-anteriorModelo18",
            data: {
                'periodo': periodo,
                'numeral': numeral,
            },
            dataType: "json",
        })
            .done(function (response) {
                if (response.descripcion.length != 0) {
                    $('#sinEntradas' + numeral).remove()
                    for (var i = 0; i < response.descripcion.length; i++) {
                        data = {}
                        data['numeral'] = response.numeral[0];
                        data['id'] = response.ids[i];

                        Modelo18.dibujar(data)
                        $("#descripcionModelo18" + response.ids[i]).val(response.descripcion[i]);
                    }
                    $("#infoAnteriorModelo18" + numeral).remove()
                    notificacion.importarPeriodo();

                }
                else {
                    notificacion.errorImportarPeriodo();
                }
            })
            .fail(function (response) {
                notificacion.error(response);
            });
    }
}
//fin modelo18
