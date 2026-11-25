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


  /* ===== Medición Meta (píxel) + dataLayer: eventos para remarketing ===== */
  var PROJ={
    'horizontes-de-manihuales':{n:'Horizontes de Mañihuales',v:28000000,r:'Aysén'},
    'dona-cecilia':{n:'Parcelación Doña Cecilia',v:19500000,r:'Maule'},
    'rofuco-bajo':{n:'Parcelas Rofuco Bajo',v:24500000,r:'Los Ríos'},
    'don-guillermo':{n:'Parcelas Don Guillermo',v:0,r:'Aysén'}
  };
  var byName={};Object.keys(PROJ).forEach(function(k){byName[PROJ[k].n]=k});
  byName['San Clemente · Parcelación Doña Cecilia']='dona-cecilia';
  var slug=document.documentElement.getAttribute('data-proyecto')||(location.pathname.match(/\/(?:proyectos|projects)\/([a-z-]+)/)||[])[1]||'';
  if(!PROJ[slug]) slug='';
  var esLanding=!!document.documentElement.getAttribute('data-proyecto');
  var base=function(s){
    var k=s||slug,o={pagina:location.pathname,idioma:lang,tipo_pagina:esLanding?'landing':(k?'proyecto':'sitio')};
    if(k&&PROJ[k]){o.content_name=PROJ[k].n;o.content_ids=[k];o.content_type='product';o.content_category='Parcelas '+PROJ[k].r;o.proyecto=k;o.region=PROJ[k].r;if(PROJ[k].v){o.value=PROJ[k].v;o.currency='CLP'}}
    return o;
  };
  var ext=function(a,b){for(var k in b) if(b.hasOwnProperty(k)) a[k]=b[k]; return a};
  // std=true: evento estándar de Meta; si no, personalizado
  var px=function(ev,params,std,opts){
    params=params||{};
    try{ if(window.fbq) window.fbq(std?'track':'trackCustom',ev,params,opts||{}); }catch(e){}
    try{ (window.dataLayer=window.dataLayer||[]).push(ext({event:ev},params)); }catch(e){}
  };
  var once={};
  var px1=function(key,ev,params,std){if(once[key])return;once[key]=1;px(ev,params,std)};
  window.pcrTrack=px;
  try{var q0=new URLSearchParams(location.search);['utm_source','utm_medium','utm_campaign','utm_content','utm_term'].forEach(function(k){if(q0.get(k)) sessionStorage.setItem('pcr_'+k,q0.get(k))})}catch(e){}

  // Ficha de proyecto o landing de campaña
  if(slug) px('ViewContent',base(),true);
  // Guías del blog y videos
  var h1=document.querySelector('h1');
  if(/\/blog\/./.test(location.pathname)) px('VerGuia',ext(base(),{guia:h1?h1.textContent.trim():''}));
  if(/videos/.test(location.pathname)) px('VerVideosPatagonia',base());
  if(/simulador|financing-simulator/.test(location.pathname)) px('VerSimulador',base());
  if(/gracias|thank-you/.test(location.pathname)) px('PaginaGracias',base());

  // Clics: WhatsApp, correo, teléfono, mapas, masterplan, redes, idioma
  document.addEventListener('click',function(e){
    var a=e.target.closest&&e.target.closest('a'); if(!a) return;
    var h=a.getAttribute('href')||'',cta=a.getAttribute('data-cta')||'',p=base();
    if(cta) p.cta=cta;
    if(/wa\.me|whatsapp\.com/.test(h)){px('Contact',ext(p,{metodo:'whatsapp'}),true);px('ClicWhatsApp',p);}
    else if(/^mailto:/.test(h)){px('Contact',ext(p,{metodo:'correo'}),true);px('ClicCorreo',p);}
    else if(/^tel:/.test(h)){px('Contact',ext(p,{metodo:'telefono'}),true);px('ClicTelefono',p);}
    else if(/maps\.app\.goo\.gl|google\.[a-z.]+\/maps|maps\.google/.test(h)){px('FindLocation',p,true);px('ComoLlegar',p);}
    else if(/masterplan|helisterra|virtualplan360/i.test(h+cta)){px('VerMasterplan',p);}
    else if(/instagram\.com|facebook\.com/.test(h)){px('ClicRedSocial',ext(p,{red:/instagram/.test(h)?'instagram':'facebook'}));}
    else if(a.classList.contains('lang')){px('CambioIdioma',p);}
    else if(a.closest('.plano,.plan-wide,figure.plan')||/plano/.test(h)){px('VerPlano',p);}
    else if(a.closest('.pcard')){var m=h.match(/(?:proyectos|projects)\/([a-z-]+)/);px('ClicProyecto',base(m&&m[1]));}
  },true);

  // Filtro de proyectos
  [].forEach.call(document.querySelectorAll('.chip[data-r]'),function(c){c.addEventListener('click',function(){px('FiltroProyectos',ext(base(),{filtro:c.dataset.r}))})});

  // Secciones vistas: precios, masterplan, mapa, galería, formulario
  if('IntersectionObserver' in window){
    var seen=[['.lots-table,.avail,.price-box','VerPrecios'],['.mp-box','VerMasterplan'],['.map-box,iframe[src*="maps"]','VerMapa'],['.gallery','VerGaleria'],['form.lead-form','VerFormulario']];
    seen.forEach(function(s){
      var el=document.querySelector(s[0]); if(!el) return;
      var o=new IntersectionObserver(function(es){es.forEach(function(x){if(x.isIntersecting){px1('sec-'+s[1],s[1],base());o.disconnect()}})},{threshold:0.35});
      o.observe(el);
    });
  }

  // Profundidad de scroll y tiempo de lectura activa
  var marks=[25,50,75,90];
  window.addEventListener('scroll',function(){
    var d=document.documentElement,pct=(window.scrollY+window.innerHeight)/d.scrollHeight*100;
    marks.forEach(function(m){if(pct>=m) px1('sc'+m,'Scroll'+m,base())});
  },{passive:true});
  var active=0,tick=setInterval(function(){
    if(document.hidden) return; active+=5;
    if(active===30) px('Tiempo30s',base());
    if(active===90){px('Tiempo90s',base());px('VisitanteComprometido',base());}
    if(active===180){px('Tiempo3min',base());clearInterval(tick);}
  },5000);

  // Videos (no cuenta el video de fondo de la portada)
  [].forEach.call(document.querySelectorAll('video'),function(v){
    if(v.closest('[data-hero-video]')) return;
    var name=(v.getAttribute('src')||v.currentSrc||'').split('/').pop();
    v.addEventListener('play',function(){px1('vp'+name,'VideoReproducido',ext(base(),{video:name}))});
    v.addEventListener('timeupdate',function(){
      if(!v.duration) return; var r=v.currentTime/v.duration;
      if(r>=0.5) px1('v50'+name,'Video50',ext(base(),{video:name}));
      if(r>=0.95) px1('v95'+name,'VideoCompleto',ext(base(),{video:name}));
    });
  });

  // Formulario: inicio (para recuperar abandonos)
  [].forEach.call(document.querySelectorAll('form.lead-form'),function(f){
    f.addEventListener('focusin',function(){
      var s=f.querySelector('select[name=proyecto]');
      px1('fi','FormularioIniciado',base(byName[s&&s.value]||slug));
    });
  });

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


  /* Simulador de crédito directo: condiciones y precios por proyecto (data-config) */
  var sim=document.getElementById('sim');
  if(sim){
    var cfg=JSON.parse(sim.dataset.config||'{}');
    var money=function(n){return '$'+Math.round(n).toLocaleString('es-CL')};
    var projEl=document.getElementById('simProject'),lotEl=document.getElementById('simLot'),plansEl=document.getElementById('simPlans');
    var qp=new URLSearchParams(location.search).get('proyecto');
    if(qp){[].forEach.call(projEl.options,function(o){if(o.value===qp)projEl.value=qp})}
    var t=lang==='en'
      ?{down:'down',inst:'instalments',mo:'/mo',msg:'Hello, I simulated direct financing for {p}, {l}: price {t}, {pct}% down ({pie}) and {n} instalments of about {c}. Could you confirm availability?'}
      :{down:'de pie',inst:'cuotas',mo:'/mes',msg:'Hola, simulé el crédito directo para {p}, {l}: precio {t}, {pct}% de pie ({pie}) y {n} cuotas de aprox. {c}. ¿Me confirman disponibilidad?'};
    var fillProject=function(){
      var c=cfg[projEl.value]||{plans:[],lots:[]};
      lotEl.innerHTML=c.lots.map(function(l,i){return '<option value="'+i+'">'+l[0]+' · '+money(l[1])+'</option>'}).join('');
      plansEl.innerHTML=c.plans.map(function(pl,i){return '<label class="plan"><input type="radio" name="plan" value="'+pl[0]+'-'+pl[1]+'"'+(i===0?' checked':'')+'><span class="plan-in"><b>'+pl[0]+'% '+t.down+'</b><span>'+pl[1]+' '+t.inst+'</span><em data-cuota="'+pl[0]+'-'+pl[1]+'">—</em></span></label>'}).join('');
      [].forEach.call(plansEl.querySelectorAll('input'),function(r){r.addEventListener('change',calc)});
      calc();
    };
    var calc=function(){
      var c=cfg[projEl.value]; if(!c||!c.lots.length) return;
      var lot=c.lots[+lotEl.value||0],price=lot[1];
      document.getElementById('simLotPrice').textContent=money(price);
      // Proyectos con precio de lista y beneficio al contado (San Clemente): se muestran por separado
      var conLista=!!c.list,box=document.getElementById('simPrices');
      if(box){box.hidden=!conLista;document.getElementById('simPriceRow').hidden=conLista;
        if(conLista){document.getElementById('simList').textContent=money(c.list);document.getElementById('simDiscount').textContent='−'+money(c.discount||0);document.getElementById('simCash').textContent=money(c.list-(c.discount||0));}}
      var lbl=document.getElementById('simTotalLbl'); if(lbl) lbl.textContent=conLista?lbl.dataset.base:lbl.dataset.price;
      var nota=document.getElementById('simNote'); if(nota){nota.hidden=!c.note;nota.textContent=c.note||'';}
      [].forEach.call(plansEl.querySelectorAll('[data-cuota]'),function(el){var k=el.dataset.cuota.split('-');el.textContent=money(price*(1-k[0]/100)/k[1])+t.mo});
      var sel=(plansEl.querySelector('input:checked')||{value:c.plans[0].join('-')}).value.split('-'),pct=+sel[0],n=+sel[1];
      var pie=price*pct/100,saldo=price-pie,cuota=saldo/n;
      document.getElementById('simCuota').textContent=money(cuota);
      document.getElementById('simPlan').textContent=n+' '+t.inst+' · '+pct+'% '+t.down;
      document.getElementById('simTotal').textContent=money(price);
      document.getElementById('simPie').textContent=money(pie);
      document.getElementById('simSaldo').textContent=money(saldo);
      var txt=t.msg.replace('{p}',projEl.value).replace('{l}',lot[0]).replace('{t}',money(price)).replace('{pct}',pct).replace('{pie}',money(pie)).replace('{n}',n).replace('{c}',money(cuota));
      document.getElementById('simWa').href='https://wa.me/56978893044?text='+encodeURIComponent(txt);
      var hid=document.querySelector('form.lead-form input[name=simulacion]'); if(hid) hid.value=txt;
    };
    var simUsed=function(){px1('sim','CustomizeProduct',base(byName[projEl.value]),true);px1('sim2','SimuladorUsado',ext(base(byName[projEl.value]),{lote:lotEl.options[lotEl.selectedIndex]&&lotEl.options[lotEl.selectedIndex].text}))};
    projEl.addEventListener('change',fillProject);
    lotEl.addEventListener('change',calc);
    sim.addEventListener('change',simUsed);
    var simWa=document.getElementById('simWa');
    if(simWa) simWa.addEventListener('click',function(){px('SimulacionWhatsApp',ext(base(byName[projEl.value]),{lote:lotEl.options[lotEl.selectedIndex]&&lotEl.options[lotEl.selectedIndex].text}))});
    fillProject();
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
      // Origen de la visita (UTM de los anuncios) para saber qué campaña generó el contacto
      var qs=new URLSearchParams(location.search);
      ['utm_source','utm_medium','utm_campaign','utm_content','utm_term'].forEach(function(k){var v=qs.get(k);try{v=v||sessionStorage.getItem('pcr_'+k)}catch(e){}if(v) fd.set(k,v)});
      fetch('https://formsubmit.co/ajax/parcelasconrio@gmail.com',{method:'POST',headers:{Accept:'application/json'},body:fd})
        .then(function(r){return r.json()})
        .then(function(j){
          if(String(j.success)!=='true') throw new Error(j.message||'error');
          var ps=f.querySelector('select[name=proyecto]'),pk=byName[ps&&ps.value]||slug,lp=base(pk),eid='lead-'+Date.now()+'-'+Math.random().toString(36).slice(2,8);
          lp.promociones=fd.get('consentimiento_promociones');
          px('Lead',lp,true,{eventID:eid});
          px('FormularioEnviado',lp);
          if(fd.get('simulacion')) px('LeadConSimulacion',lp);
          var next=f.getAttribute('data-next')||(root+(lang==='en'?'en/thank-you':'gracias'));
          setTimeout(function(){location.href=next},600);
        })
        .catch(function(){
          px('FormularioError',base());
          b.disabled=false; b.textContent=label;
          if(st) st.innerHTML=lang==='en'
            ?'We could not send your message. Please write to us on <a href="https://wa.me/56978893044" target="_blank" rel="noopener">WhatsApp</a>.'
            :'No pudimos enviar tu mensaje. Escríbenos por <a href="https://wa.me/56978893044" target="_blank" rel="noopener">WhatsApp</a>.';
        });
    });
  });
})();
