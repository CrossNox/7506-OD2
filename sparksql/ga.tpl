{%- extends 'full.tpl' -%}
{%- block html_head -%}
{{ super() }}
<div><!-- Global site tag (gtag.js) - Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=UA-128511438-1"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'UA-128511438-1');
</script>

</div>
{%- endblock -%}
