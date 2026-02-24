from django.db import models
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, InlinePanel
from modelcluster.fields import ParentalKey
from wagtail.models import Page


# ---------- DEFAULT CONTENT (portfolio demo) ----------

DEFAULT_HOME_BODY = """
<p class="lead">
  This is a demonstration website built with <strong>Django</strong> and <strong>Wagtail CMS</strong>.
  It showcases custom page templates, a blog, and a functional contact form.
</p>
<p>
  The goal of this project is to demonstrate real-world backend development,
  content management features, and cloud deployment in a clean and responsive layout.
</p>
"""

DEFAULT_ABOUT_BODY = """
<p>
  This website was developed as a practical example of a <strong>production-ready Wagtail CMS</strong> application.
</p>
<ul>
  <li>Custom page models (Home, About, Blog, Contact)</li>
  <li>Responsive Bootstrap layout</li>
  <li>Editable content through the Wagtail admin panel</li>
  <li>PostgreSQL database integration</li>
  <li>Cloud deployment using Gunicorn and Render</li>
</ul>
<p>
  The project demonstrates the core skills required for <strong>Django/Wagtail freelance development</strong>,
  including CMS customization, template work, and deployment configuration.
</p>
"""

DEFAULT_BLOG_INDEX_INTRO = """
<p>
  Welcome to the blog. Here you can find short posts about Django, Wagtail, scraping, and deployment.
</p>
"""

DEFAULT_BLOG_BODY = """
<p>
  Django and Wagtail together provide a powerful combination for building modern content-managed websites.
  Wagtail offers a flexible CMS interface, while Django handles the backend logic and database structure.
</p>
<p>
  This demo post exists to show a real blog workflow: create posts from the admin panel and publish them instantly.
</p>
"""

DEFAULT_CONTACT_INTRO = """
<p>
  Feel free to get in touch using the form below.
  This contact form is fully functional and managed through the Wagtail CMS.
</p>
<p>
  I’m available for <strong>Django</strong>, <strong>Wagtail</strong>, and <strong>Python</strong> web development projects,
  including small fixes, new features, and full website setups.
</p>
"""

DEFAULT_CONTACT_THANKYOU = """
<p>Thank you for your message! I will get back to you as soon as possible.</p>
"""


# ---------- FORMS ----------

class FormField(AbstractFormField):
    page = ParentalKey(
        "ContactPage",
        on_delete=models.CASCADE,
        related_name="form_fields",
    )


class ContactPage(AbstractEmailForm):
    intro = RichTextField(blank=True, default=DEFAULT_CONTACT_INTRO)
    thank_you_text = RichTextField(blank=True, default=DEFAULT_CONTACT_THANKYOU)

    content_panels = AbstractEmailForm.content_panels + [
        FieldPanel("intro"),
        InlinePanel("form_fields", label="Form fields"),
        FieldPanel("thank_you_text"),
        FieldPanel("from_address"),
        FieldPanel("to_address"),
        FieldPanel("subject"),
    ]


# ---------- PAGES ----------

class HomePage(Page):
    body = RichTextField(blank=True, default=DEFAULT_HOME_BODY)

    content_panels = Page.content_panels + [
        FieldPanel("body"),
    ]


class BlogPage(Page):
    body = RichTextField(blank=True, default=DEFAULT_BLOG_BODY)

    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    content_panels = Page.content_panels + [
        FieldPanel("image"),
        FieldPanel("body"),
    ]


class AboutPage(Page):
    body = RichTextField(blank=True, default=DEFAULT_ABOUT_BODY)

    content_panels = Page.content_panels + [
        FieldPanel("body"),
    ]


class BlogIndexPage(Page):
    intro = RichTextField(blank=True, default=DEFAULT_BLOG_INDEX_INTRO)

    content_panels = Page.content_panels + [
        FieldPanel("intro"),
    ]