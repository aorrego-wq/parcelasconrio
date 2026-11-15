(function(){
  var root=document.documentElement.getAttribute('data-root')||'';
  var lang=document.documentElement.lang==='en'?'en':'es';

  /* Cabecera sólida al hacer scroll */
  var top=document.querySelector('.top');
  var onScroll=function(){
    if(top&&!top.classList.contains('always')) top.classList.toggle('solid',window.scrollY>40);
    document.body.classList.toggle('scrolled',window.scrollY>500);
  };
  onScroll(); window.addEventListener('scroll',onScroll,{passive:true});

  /* Menú móvil */
  var btn=document.getElementById('menuBtn'),nav=document.getElementById('nav');
  if(btn&&nav){
    var burger=btn.innerHTML,close='<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" d="M6 6l12 12M18 6 6 18"/></svg>';
    var setMenu=function(o){nav.classList.toggle('open',o);btn.setAttribute('aria-expanded',o);btn.innerHTML=o?close:burger;btn.setAttribute('aria-label',o?(lang==='en'?'Close menu':'Cerrar menú'):(lang==='en'?'Open menu':'Abrir menú'))};
    btn.addEventListener('click',function(){setMenu(!nav.classList.contains('open'))});
    document.addEventListener('keydown',function(e){if(e.key==='Escape')setMenu(false)});
    nav.addEventListener('click',function(e){if(e.target.closest('a'))setMenu(false)});
  }

  /* Portada: video de bienvenida (versión liviana en celular) */
  var hv=document.querySelector('[data-hero-video] video');
  if(hv){
    var small=window.matchMedia('(max-width:720px)').matches;
    if(small) hv.poster=hv.dataset.posterMobile;
    if(window.matchMedia('(prefers-reduced-motion:reduce)').matches){hv.removeAttribute('autoplay')}
    else{hv.src=small?hv.dataset.mobile:hv.dataset.desktop;hv.play().catch(function(){})}
  }

  /* Filtro de proyectos por región */
  [].forEach.call(document.querySelectorAll('.chip[data-r]'),function(c){
    c.addEventListener('click',function(){
      [].forEach.call(document.querySelectorAll('.chip[data-r]'),function(x){x.classList.toggle('on',x===c)});
      [].forEach.call(document.querySelectorAll('.pcard[data-r]'),function(k){k.hidden=!(c.dataset.r==='all'||k.dataset.r===c.dataset.r)});
    });
  });

  /* Aparición suave */
  if('IntersectionObserver' in window){
    var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}})},{rootMargin:'0px 0px -8% 0px'});
    [].forEach.call(document.querySelectorAll('.reveal'),function(el){io.observe(el)});
  }else{[].forEach.call(document.querySelectorAll('.reveal'),function(el){el.classList.add('in')})}

  /* Proyecto preseleccionado desde un enlace (?proyecto=...) */
  var sel=document.querySelector('select[name="proyecto"]'),q=new URLSearchParams(location.search).get('proyecto');
  if(sel&&q){[].forEach.call(sel.options,function(o){if(o.value===q)sel.value=q})}


  /* Simulador de crédito directo: pie y cuotas sin interés (precio ingresado por el visitante) */
  var sim=document.getElementById('sim');
  if(sim){
    var money=function(n){return '$'+Math.round(n).toLocaleString('es-CL')};
    var priceEl=document.getElementById('simPrice'),projEl=document.getElementById('simProject');
    var qp=new URLSearchParams(location.search).get('proyecto');
    if(qp){[].forEach.call(projEl.options,function(o){if(o.value===qp)projEl.value=qp})}
    var t=lang==='en'
      ?{down:'down',inst:'instalments',msg:'Hello, I simulated direct financing for {p}: price {t}, {pct}% down ({pie}) and {n} instalments of about {c}. Could you confirm availability and the price?'}
      :{down:'de pie',inst:'cuotas',msg:'Hola, simulé el crédito directo para {p}: precio {t}, {pct}% de pie ({pie}) y {n} cuotas de aprox. {c}. ¿Me confirman disponibilidad y precio?'};
    var calc=function(){
      var price=parseInt((priceEl.value||'').replace(/\D/g,''),10)||0;
      if(document.activeElement!==priceEl&&price) priceEl.value=price.toLocaleString('es-CL');
      [].forEach.call(sim.querySelectorAll('[data-cuota]'),function(el){
        var k=el.dataset.cuota.split('-'),pct=+k[0],n=+k[1];
        el.textContent=price?money(price*(1-pct/100)/n)+(lang==='en'?'/mo':'/mes'):(lang==='en'?'Instalment by price':'Cuota según precio');
      });
      var sel=sim.querySelector('input[name=plan]:checked').value.split('-'),pct=+sel[0],n=+sel[1];
      var pie=price*pct/100,saldo=price-pie,cuota=saldo/n;
      var big=document.getElementById('simCuota');big.textContent=price?money(cuota):(lang==='en'?'Enter a price':'Ingresa un precio');big.classList.toggle('empty',!price);
      document.getElementById('simPlan').textContent=n+' '+t.inst+' · '+pct+'% '+t.down;
      document.getElementById('simTotal').textContent=price?money(price):'—';
      document.getElementById('simPie').textContent=price?money(pie):'—';
      document.getElementById('simSaldo').textContent=price?money(saldo):'—';
      var txt=t.msg.replace('{p}',projEl.value).replace('{t}',money(price)).replace('{pct}',pct).replace('{pie}',money(pie)).replace('{n}',n).replace('{c}',money(cuota));
      document.getElementById('simWa').href='https://wa.me/56978893044?text='+encodeURIComponent(price?txt:(lang==='en'?'Hello, I would like the price of '+projEl.value+' to simulate direct financing.':'Hola, quiero el precio de '+projEl.value+' para simular el crédito directo.'));
      var hid=document.querySelector('form.lead-form input[name=simulacion]');
      if(hid) hid.value=price?txt:'';
      var fs=document.querySelector('form.lead-form select[name=proyecto]');
      if(fs){[].forEach.call(fs.options,function(o){if(o.value===projEl.value)fs.value=projEl.value})}
    };
    priceEl.addEventListener('input',calc);
    priceEl.addEventListener('blur',calc);
    projEl.addEventListener('change',calc);
    [].forEach.call(sim.querySelectorAll('input[name=plan]'),function(r){r.addEventListener('change',calc)});
    calc();
  }

  /* Formulario: correo por FormSubmit. Contacto obligatorio; promociones opcional (se informa "no"). */
  [].forEach.call(document.querySelectorAll('form.lead-form'),function(f){
    f.addEventListener('submit',function(e){
      e.preventDefault();
      if(!f.reportValidity()) return;
      var b=f.querySelector('button[type=submit]'),st=f.querySelector('.form-status'),label=b.textContent;
      b.disabled=true; b.textContent=lang==='en'?'Sending…':'Enviando…';
      var fd=new FormData(f);
      if(!fd.has('consentimiento_promociones')) fd.set('consentimiento_promociones','no');
      fd.set('fecha_envio',new Date().toLocaleString('es-CL'));
      fd.set('pagina',location.pathname);
      fetch('https://formsubmit.co/ajax/parcelasconrio@gmail.com',{method:'POST',headers:{Accept:'application/json'},body:fd})
        .then(function(r){return r.json()})
        .then(function(j){
          if(String(j.success)!=='true') throw new Error(j.message||'error');
          location.href=root+(lang==='en'?'en/thank-you.html':'gracias.html');
        })
        .catch(function(){
          b.disabled=false; b.textContent=label;
          if(st) st.innerHTML=lang==='en'
            ?'We could not send your message. Please write to us on <a href="https://wa.me/56978893044" target="_blank" rel="noopener">WhatsApp</a>.'
            :'No pudimos enviar tu mensaje. Escríbenos por <a href="https://wa.me/56978893044" target="_blank" rel="noopener">WhatsApp</a>.';
        });
    });
  });
})();
