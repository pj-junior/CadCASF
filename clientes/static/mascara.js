  $(document).ready(function(){
  $('#id_cpf').mask('000.000.000-00');
   $('#id_celular').mask('(00) 0000-0000');   
  $('#id_cep').mask('00000-000');
 
// MASCARA DE TELEFONE --------------------- 
var SPMaskBehavior = function (val) {
return val.replace(/\D/g, '').length === 11 ? '(00) 00000-0000' : '(00) 0000-00009';
},
spOptions = {
  onKeyPress: function(val, e, field, options) {
      field.mask(SPMaskBehavior.apply({}, arguments), options);
    }
};

$('#id_telefone').mask(SPMaskBehavior, spOptions);
//-------------------------------------  
  
  
  });
