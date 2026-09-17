module.exports = async ({ page }) => {
await page.context().route("**/*", route => { const u=new URL(route.request().url()); if(u.origin === "http://127.0.0.1:8000" && ["/site_03/","/site_03/index.html"].includes(u.pathname)) return route.continue(); return route.abort(); });
};