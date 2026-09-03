# Legal & Compliance Playbook

Use this reference whenever a website collects personal data, sells goods/services, uses payments, accounts, analytics, cookies, user-generated content, advertising, email, AI, subscriptions, marketplaces, or targets a regulated/geographic market.

## Important boundary

This skill is an implementation aid, not a law firm or legal opinion. Do not invent legal requirements, claim that a template guarantees compliance, or present generated legal copy as reviewed by counsel. Identify the jurisdiction, business model, data flows, and applicable laws first. For material risk, recommend review by qualified local counsel.

## Legal-page decision matrix

Do not blindly create every page. Determine which pages are required, recommended, or conditional for the actual product.

### Common public legal pages

1. **Privacy Policy** — usually needed when personal data is collected or processed.
2. **Terms of Service / Terms & Conditions** — strongly recommended for services, SaaS, accounts, communities, apps, and transactional websites.
3. **Cookie Policy** — use when cookies/tracking technologies need separate explanation or the jurisdiction/business model calls for it.
4. **Cookie Consent / Privacy Choices** — UI/control surface where consent or opt-out mechanisms are legally required.
5. **Refund / Cancellation / Return Policy** — important for paid products, subscriptions, bookings, and e-commerce; adapt to applicable consumer law.
6. **Shipping & Delivery Policy** — for physical goods.
7. **Payment & Billing Terms** — for subscriptions, recurring billing, invoices, trials, taxes, or payment methods.
8. **Acceptable Use Policy** — for platforms, SaaS, APIs, communities, and user-generated content.
9. **Community Guidelines** — for social/community/user-generated-content products.
10. **Content / Copyright / IP Policy** — especially for UGC, publishing, marketplaces, media, or creator platforms.
11. **DMCA / Copyright Takedown Policy** — where applicable to the jurisdiction and service.
12. **Disclaimer** — where claims, advice, affiliate content, medical/financial/legal information, or third-party content creates a need for qualification.
13. **Accessibility Statement** — useful for accessibility commitments and applicable accessibility requirements.
14. **Security / Responsible Disclosure Policy** — recommended for products receiving security reports or operating APIs/platforms.
15. **Contact / Legal Notice** — business identity, legal contact, registered-office information, or other disclosures when required.
16. **Data Processing Addendum (DPA)** — generally a contractual document for qualifying processor/controller relationships, not merely a public footer page.
17. **Subprocessor List** — useful/required in some B2B privacy programs; link from privacy/DPA when applicable.
18. **Modern Slavery / ESG / other statutory disclosures** — only when the business and jurisdiction make them applicable.

### Conditional pages/features

Add only when applicable:
- Age/parental consent and children's privacy notice
- Medical/health disclaimer
- Financial/investment disclaimer
- Gambling/regulated-services disclosures
- AI transparency/AI-use notice
- Affiliate disclosure
- Advertising disclosure
- Accessibility conformance statement
- Marketplace seller terms
- Vendor/seller privacy terms
- Employment/recruitment privacy notice
- Newsletter/email consent and unsubscribe controls
- Promotional/sweepstakes terms
- Gift-card terms
- Loyalty/rewards terms
- Pre-order terms
- Booking cancellation/no-show terms
- API/developer terms

## Jurisdiction-first workflow

Before writing legal copy:

1. Identify operator/business country.
2. Identify target markets and countries/states where users are intentionally served.
3. Identify whether the site sells goods, services, subscriptions, digital content, financial/health products, or regulated services.
4. Map data collected: identity, contact, account, payment, device, location, cookies, analytics, UGC, sensitive data, children's data, AI prompts/outputs.
5. Map vendors/processors: hosting, database, auth, payments, analytics, email, storage, ads, AI, support, maps, CAPTCHA, logging.
6. Determine controller/processor or equivalent roles where relevant.
7. Determine retention, deletion, access/correction, export, consent/opt-out, and data-transfer requirements.
8. Determine consumer disclosures, cancellation/refund rules, pricing/tax disclosures, and subscription-renewal requirements.
9. Determine IP/copyright/UGC/takedown obligations.
10. Determine accessibility, marketing/email, cookie, advertising, and sector-specific obligations.
11. Link users to the actual policy pages from the footer, signup/checkout surfaces, and consent UI where appropriate.
12. Record the policy version/effective date and make material updates traceable.

## India baseline research sources

Use primary sources and verify amendments/current rules before implementation.

- India Code: central Acts and legal texts — https://www.indiacode.nic.in/
- Digital Personal Data Protection Act, 2023 — https://www.meity.gov.in/digital-personal-data-protection-act-2023
- Information Technology Act, 2000 — https://www.indiacode.nic.in/
- Consumer Protection Act, 2019 — https://www.indiacode.nic.in/
- Copyright Act, 1957 — https://www.indiacode.nic.in/
- Ministry of Electronics & Information Technology — https://www.meity.gov.in/
- Consumer Affairs — https://consumeraffairs.nic.in/
- CERT-In — https://www.cert-in.org.in/
- RBI — https://www.rbi.org.in/
- GST portal — https://www.gst.gov.in/

Do not assume that one Indian Act applies to every website. Check the business model, data processing, sector, and current subordinate rules/regulations.

## International research sources

- EU GDPR consolidated legal text — https://eur-lex.europa.eu/summary/eng/310401_2
- European Data Protection Board — https://www.edpb.europa.eu/
- European Commission data protection — https://commission.europa.eu/law/law-topic/data-protection_en
- UK ICO — https://ico.org.uk/
- UK legislation — https://www.legislation.gov.uk/
- U.S. FTC — https://www.ftc.gov/
- U.S. NIST Privacy Framework — https://www.nist.gov/privacy-framework
- California Privacy Protection Agency — https://cppa.ca.gov/
- California legislative information — https://leginfo.legislature.ca.gov/

These are research starting points, not a universal checklist. Applicability varies by jurisdiction and facts.

## Technical/privacy implementation rules

### Privacy

- Inventory every collection point.
- State purpose and lawful/legitimate basis as applicable.
- Avoid collecting data that the product does not need.
- Provide applicable rights/choice mechanisms.
- Document retention/deletion behavior.
- Explain third-party sharing and categories of recipients.
- Explain international transfers when relevant.
- Keep privacy policy claims synchronized with actual code/configuration.

### Cookies and tracking

- Inventory cookies, SDKs, pixels, local storage, fingerprinting-like mechanisms, and analytics.
- Classify technologies according to the target jurisdiction and actual purpose.
- Do not fire consent-dependent tracking before the required consent/choice is obtained.
- Provide an understandable settings/withdrawal mechanism where required.
- Keep the consent state auditable without storing unnecessary personal data.

### Accounts and authentication

- Explain account data and security practices accurately.
- Provide account deletion/export mechanisms where applicable.
- Do not claim passwords are stored in plaintext-free form unless implementation actually supports the claim.

### Payments and subscriptions

- Show price, billing interval, taxes/fees where required, trial conversion, renewal, cancellation, and refund terms clearly.
- Never trust client-side price or discount values.
- Keep payment credentials out of the application when using a hosted/tokenized payment provider.
- Make recurring billing/webhook handling idempotent.

### UGC and copyright

- Define prohibited content and moderation rules.
- Define reporting/takedown paths.
- Store evidence and audit events proportionately.
- Do not copy copyrighted text, images, trademarks, or legal templates from third parties without permission or an appropriate license.

### AI products

- Document what user content is sent to AI providers when material.
- Avoid claiming confidentiality or training behavior unless verified in the provider terms/configuration.
- Provide abuse/safety boundaries appropriate to the product.
- Consider disclosure when users may reasonably believe they are interacting with a human.
- Keep high-risk professional advice qualified and appropriately reviewed.

## Legal-page UX requirements

- Put legal links in the global footer where appropriate.
- Make links keyboard accessible and readable on mobile.
- Show an effective/updated date when appropriate.
- Keep headings and sections scannable.
- Use plain language; define legal terms where possible.
- Provide contact/rights-request channels where required.
- Do not bury material pricing, renewal, cancellation, or consent information only in a long policy.
- Localize policy language when serving materially different markets.
- Avoid dark patterns around consent, cancellation, or privacy choices.

## Verification checklist

Before declaring legal/compliance work complete:

- [ ] Jurisdiction and target markets identified.
- [ ] Data inventory matches actual code.
- [ ] Vendors/processors match actual integrations.
- [ ] Privacy/cookie behavior matches the policy.
- [ ] Consent/opt-out controls work where applicable.
- [ ] Signup/checkout contains required disclosures.
- [ ] Refund/cancellation/renewal behavior matches the stated terms.
- [ ] UGC/copyright reporting exists when needed.
- [ ] Legal links are discoverable from relevant pages.
- [ ] Effective dates/versioning are correct.
- [ ] No unsupported legal guarantee is stated.
- [ ] Current primary legal sources were checked for amendments/rules.
- [ ] Material legal questions are flagged for professional review.

## Official-source rule

When a legal requirement affects implementation, prefer the controlling statute/regulation or official regulator guidance over blogs, template generators, SEO articles, or remembered summaries. Record the source and access date in project notes when the decision is material.
