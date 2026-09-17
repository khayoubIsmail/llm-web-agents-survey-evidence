module.exports = async ({ page }) => {
await page.context().route("**/*", route => { const u=new URL(route.request().url()); if(u.origin === "http://127.0.0.1:8000" && ["/site_04/","/site_04/index.html"].includes(u.pathname)) return route.continue(); return route.abort(); });
};