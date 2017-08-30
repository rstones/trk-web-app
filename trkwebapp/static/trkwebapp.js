window.onload = function() {
	
	var renderer = new X.renderer3D();
	renderer.container = 'trk-renderer';
	renderer.config.PICKING_ENABLED = false;
	renderer.init();
	
	trk = new X.fibers();
	trk.file = 'get_trk?.trk';
	trk.opacity = 1.0;
	
	renderer.add(trk);
	renderer.render();
}