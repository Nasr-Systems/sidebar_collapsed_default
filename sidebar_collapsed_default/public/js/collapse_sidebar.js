frappe.provide('frappe.ui.pages');

const originalSetupSidebarToggle = frappe.ui.Page.prototype.setup_sidebar_toggle;

// Overriding the setup_sidebar_toggle function in frappe.ui.Page.prototype
frappe.ui.Page.prototype.setup_sidebar_toggle = function () {

    // Select the sidebar toggle button within the page head
    let sidebar_toggle = $(".page-head").find(".sidebar-toggle-btn");

    // Select the sidebar wrapper element within the page layout
    let sidebar_wrapper = this.wrapper.find(".layout-side-section");

    // Toggle the visibility of the sidebar wrapper
    sidebar_wrapper.toggle();

    // Check if the sidebar toggle functionality is disabled or if there's no sidebar wrapper element
    if (this.disable_sidebar_toggle || !sidebar_wrapper.length) {
        // If either condition is true, remove the last sidebar toggle button
        sidebar_toggle.last().remove();
    } else {
        // If the sidebar is not disabled and there is a sidebar wrapper element

        // If not a mobile device, set a title attribute on the sidebar toggle for accessibility
        if (!frappe.is_mobile()) {
            sidebar_toggle.attr("title", __("Toggle Sidebar"));
        }

        // Set an ARIA label for accessibility
        sidebar_toggle.attr("aria-label", __("Toggle Sidebar"));

        // Initialize a tooltip for the sidebar toggle with delay and hover trigger settings
        sidebar_toggle.tooltip({
            delay: { show: 600, hide: 100 },
            trigger: "hover",
        });

        // Add a click event listener to the sidebar toggle button
        sidebar_toggle.click(() => {
            // Check if the screen size is extra small (xs) or small (sm)
            if (frappe.utils.is_xs() || frappe.utils.is_sm()) {
                // If the screen size is xs or sm, set up an overlay sidebar
                this.setup_overlay_sidebar();
            } else {
                // Otherwise, simply toggle the visibility of the sidebar wrapper
                sidebar_wrapper.toggle();
            }

            // Trigger the toggleSidebar event on the document body
            $(document.body).trigger("toggleSidebar");

            // Update the sidebar toggle icon 
            this.update_sidebar_icon();
        });
    }
};