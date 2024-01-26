import React from "react";

const Testimonials = () => {
  return (
    <div className="container mx-auto mt-20">
      <div className="mx-auto max-w-screen-xl px-4 py-12 sm:px-6 lg:px-8 lg:py-16">
        <h2 className="text-center text-2xl font-bold tracking-tight text-gray-900 sm:text-2xl">
          What our users say about us;
        </h2>

        <div className="mt-8 grid grid-cols-1 gap-4 md:grid-cols-3 md:gap-8">
          <blockquote className="rounded-lg bg-white p-6 shadow-md sm:p-8">
            <div className="flex items-center gap-4">
              <img
                alt="User"
                src="https://img.freepik.com/free-photo/portrait-young-woman-with-natural-make-up_23-2149084942.jpg"
                className="h-14 w-14 rounded-full object-cover"
              />

              <div>
                <p className="mt-0.5 text-lg font-medium text-gray-900">
                  Sarah Johnson
                </p>
                <p className="mt-0.5 text-sm font-small text-gray-500">
                  Home Cook
                </p>
              </div>
            </div>

            <p className="mt-4 text-gray-700">
              I can't believe how much I've learned from the recipes on this
              app. The variety is amazing, and the recipes are easy to follow.
              Thank you, BiteBinders, for this incredible opportunity!
            </p>
          </blockquote>

          <blockquote className="rounded-lg bg-white p-6 shadow-md sm:p-8">
            <div className="flex items-center gap-4">
              <img
                alt="User"
                src="https://images.unsplash.com/photo-1595152772835-219674b2a8a6?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1180&q=80"
                className="h-14 w-14 rounded-full object-cover"
              />

              <div>
                <p className="mt-0.5 text-lg font-medium text-gray-900">
                  David Clark
                </p>

                <p className="mt-0.5 text-sm font-small text-gray-500">
                  Food Blogger
                </p>
              </div>
            </div>

            <p className="mt-4 text-gray-700">
              I stumbled upon this app while searching for new recipes. The
              variety of dishes and the user-friendly design are exceptional.
              Thanks to BiteBinders, I've discovered a plethora of new dishes!
            </p>
          </blockquote>

          <blockquote className="rounded-lg bg-white p-6 shadow-md sm:p-8">
            <div className="flex items-center gap-4">
              <img
                alt="User"
                src="https://web-images.pixpa.com/ajHEWPBxk0_3pRaLCAKZ33oKmOUHMRwjRHKT8Le_UL0/rs:fit:1200:0/q:80/czM6Ly9waXhwYS5jb20vL2NvbS9hcnRpY2xlcy8xNTI1ODkxODc5LTE1MDQ0NC1vbGFkaW1lamktb2R1bnNpLTQxNTYwNi11bnNwbGFzaGpwZy5qcGc="
                className="h-14 w-14 rounded-full object-cover"
              />

              <div>
                <p className="mt-0.5 text-lg font-medium text-gray-900">
                  Emily Turner
                </p>

                <p className="mt-0.5 text-sm font-small text-gray-500">
                  Professional Chef
                </p>
              </div>
            </div>

            <p className="mt-4 text-gray-700">
              As a professional chef, I'm always on the lookout for new recipes
              and culinary inspirations. BiteBinders has been an invaluable
              resource. The diversity of recipes and the quality of the content
              are unbeatable. I'm so grateful for this app!
            </p>
          </blockquote>
        </div>
      </div>
    </div>
  );
};

export default Testimonials;
