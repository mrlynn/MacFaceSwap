import { blogPosts } from '../../../lib/blog-data';
import { ArrowLeft, Clock, Calendar } from 'lucide-react';

export async function generateStaticParams() {
  return Object.keys(blogPosts).map((slug) => ({
    slug: slug,
  }));
}

export default function BlogPostPage({ params }) {
  const post = blogPosts[params.slug];

  if (!post) {
    return (
      <div className="min-h-screen bg-gradient-to-br from-purple-900 to-pink-700 text-white">
        <div className="container mx-auto px-4 py-16 text-center">
          <h1 className="text-4xl font-bold mb-4">Post Not Found</h1>
          <a 
            href="../../"
            className="text-pink-300 hover:text-pink-400 inline-flex items-center gap-2"
          >
            <ArrowLeft size={20} />
            Return to Home
          </a>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-purple-900 to-pink-700">
      {/* Navigation */}
      <nav className="container mx-auto px-4 py-6">
        <div className="flex justify-between items-center">
          <a 
            href="../../"
            className="inline-flex items-center gap-2 text-white hover:text-pink-300"
          >
            <ArrowLeft size={20} />
            Home
          </a>
          <a 
            href="../"
            className="text-white hover:text-pink-300"
          >
            All Posts
          </a>
        </div>
      </nav>

      {/* Article Container with White Background */}
      <div className="container mx-auto px-4 py-8">
        <article className="bg-white rounded-2xl shadow-xl overflow-hidden">
          {/* Header Image Section */}
          <div className="px-8 pt-8">
            <div className="rounded-xl overflow-hidden shadow-lg">
              <img
                src={post.headerImage.src}
                alt={post.headerImage.alt}
                className="w-full h-[400px] object-cover"
              />
            </div>
          </div>

          {/* Article Content */}
          <div className="px-8 py-12">
            <header className="mb-12">
              <div className="flex items-center gap-4 mb-4">
                <span className="bg-pink-500 text-white px-3 py-1 rounded-full text-sm">
                  {post.category}
                </span>
                <div className="flex items-center gap-4 text-gray-600">
                  <span className="flex items-center gap-1">
                    <Calendar size={16} />
                    {post.date}
                  </span>
                  <span className="flex items-center gap-1">
                    <Clock size={16} />
                    {post.readTime}
                  </span>
                </div>
              </div>
              <h1 className="text-4xl font-bold mb-6 text-gray-900">{post.title}</h1>
              <p className="text-xl text-gray-600">{post.excerpt}</p>
            </header>

            <div 
              className="prose max-w-none"
              dangerouslySetInnerHTML={{ __html: post.content }}
            />
          </div>
        </article>
      </div>
    </div>
  );
}