//Variables
var leftMenu = document.getElementById("left-menu");
var btnPanel = document.getElementById("btn-show-panel");
var body = document.getElementById("body");
var content = document.getElementById("content-page-id");
var header = document.getElementById("header-container-id");

var btnHome = document.getElementById("btn-home");
var btnCategoria = document.getElementById("btn-categoria");
var btnCliente = document.getElementById("btn-cliente");
var btnCompra = document.getElementById("btn-compra");
var btnCotizacion = document.getElementById("btn-cotizacion");
var btnDescuento = document.getElementById("btn-descuento")
var btnDireccion = document.getElementById("btn-direccion");
var btnEmpleado = document.getElementById("btn-empleado");
var btnPago = document.getElementById("btn-pago");
var btnProducto = document.getElementById("btn-producto");
var btnProveedor = document.getElementById("btn-proveedor");
var btnSucursal = document.getElementById("btn-sucursal");
var btnTelefono = document.getElementById("btn-telefono");
var btnVenta = document.getElementById("btn-venta");

//Evento para mostrar menú
btnPanel.addEventListener("click",showMenu);

//Funcion mostrar menú
function showMenu(){
    body.classList.toggle("show-menu-body");
    leftMenu.classList.toggle("show-menu");
    btnPanel.classList.toggle("open");
    content.classList.toggle("respo-content");
    header.classList.toggle("respo-header");
}

function getParameter(parameterName){
    let parameters = new URLSearchParams(window.location.search);
    return parameters.get(parameterName);
}

let parameter = getParameter("b");
function selectedButton(){
    if(parameter=="home"){
        btnHome.classList.toggle("selected");
    }else if(parameter=="categoria"){
        btnCategoria.classList.toggle("selected");
    }else if(parameter=="cliente"){
        btnCliente.classList.toggle("selected");
    }else if(parameter=="compra"){
        btnCompra.classList.toggle("selected");
    }else if(parameter=="cotizacion"){
        btnCotizacion.classList.toggle("selected");
    }else if(parameter=="descuento"){
        btnDescuento.classList.toggle("selected");
    }else if(parameter=="empleado"){
        btnEmpleado.classList.toggle("selected");
    }else if(parameter=="pago"){
        btnPago.classList.toggle("selected");
    }else if(parameter=="producto"){
        btnProducto.classList.toggle("selected");
    }else if(parameter=="proveedor"){
        btnProveedor.classList.toggle("selected");
    }else if(parameter=="sucursal"){
        btnSucursal.classList.toggle("selected");
    }else if(parameter=="venta"){
        btnVenta.classList.toggle("selected");
    }
}

selectedButton();